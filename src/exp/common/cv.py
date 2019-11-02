import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import lightgbm as lgb
import xgboost as xgb


def cv(cv_df=pd.DataFrame(), model_name="linearRegression", params={}):

    print("----------------", model_name, "----------------")
    result = pd.DataFrame()
    scores = []
    for n_fold in cv_df["n_fold"].unique():
        df = cv_df[cv_df["n_fold"] == n_fold]
        train = df[df["data_type"] == "train"].drop(
            ["target", "data_type", "index"], axis=1
        )
        val = df[df["data_type"] == "val"].drop(
            ["target", "data_type", "index"], axis=1
        )
        y_train = df[df["data_type"] == "train"]["target"].values
        y_val = df[df["data_type"] == "val"]["target"].values

        if model_name == "linearRegression":
            model = LinearRegression()
            model.fit(train, np.log(y_train))
            y_pred = np.exp(model.predict(val))

        if model_name == "lightgbm":
            lgb_train = lgb.Dataset(train, y_train.flatten(), params={"verbose": -1})
            lgb_eval = lgb.Dataset(
                val, y_val.flatten(), reference=lgb_train, params={"verbose": -1}
            )

            gbm = lgb.train(
                params,
                lgb_train,
                num_boost_round=100,
                valid_sets=lgb_eval,
                early_stopping_rounds=10,
                verbose_eval=False,
            )

            y_pred = gbm.predict(val, num_iteration=gbm.best_iteration)

        if model_name == "xgboost":
            dtrain = xgb.DMatrix(train, label=y_train.flatten())
            dtest = xgb.DMatrix(val, label=y_val.flatten())
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
                        "index": df[df["data_type"] == "val"]["index"],
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
