# age : to float value
def pp_age(df):
    age = df["age"]

    age = age.map(lambda x: "0年" if x == "新築" else x)

    y_m = age.str.split("年", expand=True)
    year = y_m.iloc[:, 0].astype(int)
    month = (
        y_m.iloc[:, 1]
        .str.replace("ヶ月", "")
        .map(lambda x: "0" if x == "" else x)
        .astype(int)
    )

    df.loc[:, "age"] = year + month / 12

    df.loc[df["age"] > 70, "age"] = 70
    return df
