import pandas as pd


# kitchen : One-Hot Enfoding
def pp_kitchen(df):
    kitchen = df["kitchen"]
    kitchen = kitchen.str.replace("／", "")

    # Create unique values list
    bathroom_unique = pd.Series(
        pd.Series(kitchen.str.split("\t", expand=True).values.flatten()).unique()
    )
    # drop None, NaN, and ''
    bathroom_unique = bathroom_unique[~bathroom_unique.isnull()]
    bathroom_unique = bathroom_unique[bathroom_unique != ""]

    # One-Hot Encoding
    for col_name in bathroom_unique:
        df.loc[:, "ohe_kitchen_" + col_name] = (
            df["kitchen"].fillna("").str.contains(col_name).astype(int)
        )

    return df
