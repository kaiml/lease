import lightgbm as lgb
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import StratifiedKFold


def cross_validation(train_df, model_name="linearRegression", params=None):
    print("----------------", model_name, "----------------")
    result = pd.DataFrame()
    scores = []
    y = train_df["target"].values
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=0).split(train_df, y)
    for n_fold, (train_index, val_index) in enumerate(folds):
        train = train_df.loc[train_index]
        val = train_df.loc[val_index]
        y_train = y[train_index]
        y_val = y[val_index]

        if model_name == "linearRegression":
            model = LinearRegression()
            model.fit(train.drop(["target"], axis=1), np.log(y_train))
            y_pred = np.exp(model.predict(val.drop(["target"], axis=1)))

        if model_name == "lightgbm":
            lgb_train = lgb.Dataset(
                train.drop(["target"], axis=1),
                y_train.flatten(),
                params={"verbose": -1},
            )
            lgb_eval = lgb.Dataset(
                val.drop(["target"], axis=1),
                y_val.flatten(),
                reference=lgb_train,
                params={"verbose": -1},
            )

            gbm = lgb.train(
                params,
                lgb_train,
                num_boost_round=100,
                valid_sets=lgb_eval,
                early_stopping_rounds=10,
                verbose_eval=False,
            )

            y_pred = gbm.predict(
                val.drop(["target"], axis=1), num_iteration=gbm.best_iteration
            )

        if model_name == "xgboost":
            dtrain = xgb.DMatrix(
                train.drop(["target"], axis=1), label=y_train.flatten()
            )
            dtest = xgb.DMatrix(val.drop(["target"], axis=1), label=y_val.flatten())
            gbm = xgb.train(params, dtrain, num_boost_round=100)  # 学習ラウンド数は適当
            y_pred = gbm.predict(dtest)

        score = np.sqrt(
            ((y_pred.flatten() - y_val.flatten()) ** 2).sum() / len(y_val.flatten())
        )
        scores.append(score)
        print("n_fold: {} Score: {}".format(n_fold, score))

        result = pd.concat(
            [
                result,
                pd.DataFrame(
                    {
                        "index": val_index,
                        "predicted": y_pred.flatten(),
                        "real": y_val.flatten(),
                        "difference": y_pred.flatten() - y_val.flatten(),
                        "n_fold": n_fold,
                    }
                ),
            ]
        )

    print("----------------", model_name, " END ----------------")
    print()
    return result, scores
