import pandas as pd


def one_hot_encoding(df=pd.DataFrame(), col_name=""):
    df = pd.concat([df, pd.get_dummies(df[col_name], prefix="ohe_" + col_name)], axis=1)
    return df
