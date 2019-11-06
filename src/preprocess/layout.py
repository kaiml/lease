# layout : delete "+S(納戸)"
def pp_layout(df):
    df.loc[:, "layout"] = df["layout"].str.replace("\+S\(納戸\)", "")
    df.loc[
        (df["layout"] == "4K")
        | (df["layout"] == "4DK")
        | (df["layout"] == "4LDK")
        | (df["layout"] == "5K")
        | (df["layout"] == "5DK")
        | (df["layout"] == "5LDK")
        | (df["layout"] == "6LDK"),
        "layout",
    ] = "4K以上"
    df.loc[(df["layout"] == "1LK") | (df["layout"] == "1R"), "layout"] = "1K"

    return df
