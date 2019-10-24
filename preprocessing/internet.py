import pandas as pd


# internet : One-Hot Encoding
def pp_internet(df):
    internet = df["internet"]
    internet = internet.str.replace("／", "")

    # Create unique values list
    bathroom_unique = pd.Series(
        pd.Series(internet.str.split("\t", expand=True).values.flatten()).unique()
    )
    # drop None, NaN, and ''
    bathroom_unique = bathroom_unique[~bathroom_unique.isnull()]
    bathroom_unique = bathroom_unique[bathroom_unique != ""]

    # One-Hot Encoding
    for col_name in bathroom_unique:
        df.loc[:, "ohe_internet_" + col_name] = (
            df["internet"].fillna("").str.contains(col_name).astype(int)
        )

    return df
