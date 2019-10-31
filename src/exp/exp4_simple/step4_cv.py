import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold

import xgboost as xgb


def step4_cv(train_df):
    # xgb parameters
    params = {
        # 回帰問題
        "objective": "reg:squarederror",
        # 学習用の指標 (RMSE)
        "eval_metric": "rmse",
    }
    result = pd.DataFrame()
    scores = []
    y = train_df["target"].values
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=0).split(train_df, y)
    for n_fold, (train_index, val_index) in enumerate(folds):
        train = train_df.loc[train_index]
        val = train_df.loc[val_index]
        y_train = y[train_index]
        y_val = y[val_index]

        dtrain = xgb.DMatrix(train.drop(["target"], axis=1), label=y_train.flatten())
        dtest = xgb.DMatrix(val.drop(["target"], axis=1), label=y_val.flatten())

        gbm = xgb.train(params, dtrain, num_boost_round=100)  # 学習ラウンド数は適当

        y_pred = gbm.predict(dtest)

        score = np.sqrt(
            ((y_pred.flatten() - y_val.flatten()) ** 2).sum() / len(y_val.flatten())
        )
        scores.append(score)
        print("No.{} Score: {}".format(n_fold, score))

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

    return result, scores
