import pandas as pd


def fill_missing_data(df=pd.DataFrame(), col_name="", method="most_frequent"):
    # fill NaN with most frequent values
    if method == "most_frequent":
        df.loc[:, col_name] = df[col_name].fillna(df[col_name].value_counts().index[0])

    return df
