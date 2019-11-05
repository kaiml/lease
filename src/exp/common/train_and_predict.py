import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import lightgbm as lgb
import xgboost as xgb


def train_and_predict(
    train_x=pd.DataFrame(),
    train_y=pd.Series(),
    val_x=pd.DataFrame(),
    model_name="linearRegression",
    params={},
):
    if model_name == "linearRegression":
        model = LinearRegression()
        model.fit(train_x, np.log(train_y))
        y_pred = np.exp(model.predict(val_x))

    if model_name == "lightgbm":
        lgb_train = lgb.Dataset(train_x, train_y, params={"verbose": -1})
        model = lgb.train(
            params,
            lgb_train,
            verbose_eval=False,
        )
        y_pred = model.predict(val_x, num_iteration=model.best_iteration)

    if model_name == "xgboost":
        dtrain = xgb.DMatrix(train_x, label=train_y)
        dtest = xgb.DMatrix(val_x)
        model = xgb.train(params, dtrain, num_boost_round=100)  # 学習ラウンド数は適当
        y_pred = model.predict(dtest)

    return y_pred, model
