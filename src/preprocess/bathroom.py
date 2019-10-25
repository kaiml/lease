import pandas as pd


# bathroom: One-Hot Encoding
def pp_bathroom(df):
    bathroom = df["bathroom"]
    bathroom = bathroom.str.replace("／", "")

    # Create unique values list
    bathroom_unique = pd.Series(
        pd.Series(bathroom.str.split("\t", expand=True).values.flatten()).unique()
    )
    # drop None, NaN, and ''
    bathroom_unique = bathroom_unique[~bathroom_unique.isnull()]
    bathroom_unique = bathroom_unique[bathroom_unique != ""]

    # One-Hot Encoding
    for col_name in bathroom_unique:
        df.loc[:, "ohe_bathroom_" + col_name] = (
            df["bathroom"].fillna("").str.contains(col_name).astype(int)
        )

    return df
