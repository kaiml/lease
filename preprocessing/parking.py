def pp_parking(df):
    parking = df["parking"].fillna("")
    df.loc[:, "ohe_parking_駐車場"] = parking.str.contains("駐車場\t空有").astype(int)
    df.loc[:, "ohe_parking_駐輪場"] = parking.str.contains("駐輪場\t空有").astype(int)
    return df
