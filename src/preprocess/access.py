import numpy as np


# access : to line_1,2,3, station_1,2,3, duration_1,2,3, is_bus_1,2,3
def pp_access(df):
    def to_hankaku(text):
        return text.translate(
            str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})
        )

    access = df["access"]
    access_split = access.str.split("\t", expand=True)
    line_1 = access_split.iloc[:, 0]
    station_1 = access_split.iloc[:, 1]
    station_1 = station_1.str.replace(r"\(.*\)", "")  # 町屋(東京メトロ)駅 -> 町屋駅
    duration_1 = access_split.iloc[:, 2]
    duration_1 = duration_1.map(to_hankaku)
    walk_1 = (
        duration_1.str.extract(r"(徒歩\d{1,3}分)")
        .iloc[:, 0]
        .fillna("")
        .str.extract(r"(\d{1,3})")
        .fillna(0)
        .astype(int)
        .iloc[:, 0]
    )
    bus_1 = (
        duration_1.str.extract(r"(\/バス\(\d{1,3}分\))")
        .iloc[:, 0]
        .fillna("")
        .str.extract(r"(\d{1,3})")
        .fillna(0)
        .astype(int)
        .iloc[:, 0]
    )
    is_bus_1 = (bus_1 != 0).astype(int)
    duration_1 = walk_1 + bus_1 * 10

    line_2 = access_split.iloc[:, 4].fillna(np.nan)
    station_2 = access_split.iloc[:, 5]
    station_2 = station_2.str.replace(r"\(.*\)", "")  # 町屋(東京メトロ)駅 -> 町屋駅
    station_2 = station_2.fillna(np.nan)
    duration_2 = access_split.iloc[:, 6]
    walk_2 = (
        duration_2.str.extract(r"(徒歩\d{1,3}分)")
        .iloc[:, 0]
        .fillna("")
        .str.extract(r"(\d{1,3})")
        .astype(float)
        .iloc[:, 0]
    )
    bus_2 = (
        duration_2.str.extract(r"(\/バス\(\d{1,3}分\))")
        .iloc[:, 0]
        .fillna("")
        .str.extract(r"(\d{1,3})")
        .fillna(0)
        .astype(int)
        .iloc[:, 0]
    )
    is_bus_2 = (bus_2 != 0).astype(int)
    duration_2 = walk_2 + bus_2 * 10

    line_3 = access_split.iloc[:, 8].fillna(np.nan)
    station_3 = access_split.iloc[:, 9]
    station_3 = station_3.str.replace(r"\(.*\)", "")  # 町屋(東京メトロ)駅 -> 町屋駅
    station_3 = station_3.fillna(np.nan)
    duration_3 = access_split.iloc[:, 6]
    walk_3 = (
        duration_3.str.extract(r"(徒歩\d{1,3}分)")
        .iloc[:, 0]
        .fillna("")
        .str.extract(r"(\d{1,3})")
        .astype(float)
        .iloc[:, 0]
    )
    bus_3 = (
        duration_3.str.extract(r"(\/バス\(\d{1,3}分\))")
        .iloc[:, 0]
        .fillna("")
        .str.extract(r"(\d{1,3})")
        .fillna(0)
        .astype(int)
        .iloc[:, 0]
    )
    is_bus_3 = (bus_3 != 0).astype(int)
    duration_3 = walk_3 + bus_3 * 10

    df.loc[:, "line_1"] = line_1
    df.loc[:, "station_1"] = station_1
    df.loc[:, "duration_1"] = duration_1
    df.loc[:, "is_bus_1"] = is_bus_1

    df.loc[:, "line_2"] = line_2
    df.loc[:, "station_2"] = station_2
    df.loc[:, "duration_2"] = duration_2
    df.loc[:, "is_bus_2"] = is_bus_2

    df.loc[:, "line_3"] = line_3
    df.loc[:, "station_3"] = station_3
    df.loc[:, "duration_3"] = duration_3
    df.loc[:, "is_bus_3"] = is_bus_3

    df["duration_1_1min"] = (df["duration_1"] <= 1).astype(int)
    df["duration_1_3min"] = ((1 < df["duration_1"]) & (df["duration_1"] <= 3)).astype(
        int
    )
    df["duration_1_5min"] = ((3 < df["duration_1"]) & (df["duration_1"] <= 5)).astype(
        int
    )
    df["duration_1_7min"] = ((5 < df["duration_1"]) & (df["duration_1"] <= 7)).astype(
        int
    )
    df["duration_1_10min"] = ((7 < df["duration_1"]) & (df["duration_1"] <= 10)).astype(
        int
    )
    df["duration_1_15min"] = (
        (10 < df["duration_1"]) & (df["duration_1"] <= 15)
    ).astype(int)
    df["duration_1_20min"] = (
        (15 < df["duration_1"]) & (df["duration_1"] <= 20)
    ).astype(int)
    df["duration_1_more_than_20min"] = (20 < df["duration_1"]).astype(int)

    df.loc[:, "station_2"] = df["station_2"].fillna(df["station_1"])

    return df
