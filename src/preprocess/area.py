# area : to float value
def pp_area(df):
    area = df["area"]
    area = area.str.replace("m2", "")
    area = area.astype(float)

    df.loc[:, "area"] = area
    # df.loc[df.area > 200, "area"] = 200
    return df
