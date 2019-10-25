import numpy as np
import pandas as pd


def rename_cols(df):
    df = df.rename(columns={"賃料": "target"})
    return df


# 面積
def pre_area(df):
    df.loc[:, "area"] = df["面積"].str.replace("m2", "").astype(float)
    return df


# 方角
def pre_direction(df):
    df.loc[:, "direction"] = df["方角"]
    return df


# 区
def pre_ward(df):
    # oo区
    df.loc[:, "ward"] = df["所在地"].str.replace("東京都", "").str.split("区", expand=True)[0]
    # oo区oo
    df.loc[:, "ward_detail"] = (
        df["所在地"].str.replace("東京都", "").str.split(r"\d", n=1, expand=True).iloc[:, 0]
    )
    return df


# 間取り
def pre_madori(df):
    df.loc[:, "nando"] = df["間取り"].str.contains("納戸").astype(int)
    df.loc[:, "madori"] = df["間取り"].str.replace("(納戸)", "").str.replace("+", "")
    return df


# キッチン
def pre_kitchen(df):
    for kitchen_col_name in pd.Series(
        df["キッチン"].str.replace("／", "").str.split("\t", expand=True).values.flatten()
    ).unique():
        if (
            kitchen_col_name
            and type(kitchen_col_name) == str
            and kitchen_col_name != ""
        ):
            df.loc[:, kitchen_col_name] = (
                df["キッチン"].fillna("").str.contains(kitchen_col_name).astype(int)
            )
    return df


# バス・トイレ
def pre_bath(df):
    for bath_col_name in pd.Series(
        df["バス・トイレ"].str.replace("／", "").str.split("\t", expand=True).values.flatten()
    ).unique():
        if (
            bath_col_name
            and type(bath_col_name) == str
            and bath_col_name != ""
            and bath_col_name != "トイレなし"
        ):
            df.loc[:, bath_col_name] = (
                df["バス・トイレ"].fillna("").str.contains(bath_col_name).astype(int)
            )
    return df


# 室内設備
def pre_room_equip(df):
    for bath_col_name in pd.Series(
        df["室内設備"].str.replace("／", "").str.split("\t", expand=True).values.flatten()
    ).unique():
        if bath_col_name and type(bath_col_name) == str and bath_col_name != "":
            df.loc[:, bath_col_name] = (
                df["室内設備"].fillna("").str.contains(bath_col_name).astype(int)
            )
    return df


# 放送・通信
def pre_comm(df):
    for comm_col_name in pd.Series(
        df["放送・通信"].str.replace("／", "").str.split("\t", expand=True).values.flatten()
    ).unique():
        if comm_col_name and type(comm_col_name) == str and comm_col_name != "":
            df.loc[:, comm_col_name] = (
                df["放送・通信"].fillna("").str.contains(comm_col_name).astype(int)
            )
    return df


# 契約期間
def pre_contract_period(df):
    df.loc[:, "contract_period"] = df["契約期間"].map(
        lambda x: np.nan
        if type(x) == float or "まで" in x
        else x.replace("※この物件は\t定期借家\tです。", "").replace("\t", "").replace("間", "")
    )

    def contract_period_to_float(x):
        if type(x) == float:
            return x

        elif len(x.split("年")) == 2 and x.split("年")[1] == "":
            return float(x.replace("年", ""))

        elif len(x.split("ヶ月")) == 2 and x.split("ヶ月")[1] == "" and "年" not in x:
            return float(x.replace("ヶ月", "")) / 12

        else:
            return (
                float(x.split("年")[0]) + float(x.split("年")[1].replace("ヶ月", "")) / 12
            )

    df.loc[:, "contract_period"] = df["contract_period"].map(contract_period_to_float)
    df.loc[:, "teiki_shakuya"] = (
        df["契約期間"]
        .str.contains("定期借家")
        .map(lambda x: np.nan if type(x) == float else float(x))
    )
    return df


# アクセス
def pre_access(df):
    # アクセスに関する列を抽出
    df_access = df["アクセス"].str.split("\t", expand=True)[[0, 1, 2, 4, 5, 6, 8, 9, 10]]

    df_access.columns = [
        "line_1",
        "station_1",
        "duration_1",
        "line_2",
        "station_2",
        "duration_2",
        "line_3",
        "station_3",
        "duration_3",
    ]

    # 1つめの最寄り駅がバス/車の場合はNaNに
    df_access.loc[:, "duration_1"] = df_access.loc[:, "duration_1"].str.replace(
        "徒歩", ""
    )
    df_access.loc[
        (
            df_access["duration_1"].str.contains("バス")
            | df_access["duration_1"].str.contains("車")
        ),
        ["line_1", "station_1", "duration_1"],
    ] = ["", "", ""]
    df_access.loc[:, "station_1"] = df_access["station_1"].str.replace("駅", "")
    df_access.loc[:, "duration_1"] = (
        df_access["duration_1"]
        .map(lambda x: np.nan if x == "" else x.replace("徒歩", "").replace("分", ""))
        .astype(float)
    )

    # 2つめの最寄り駅がバス/車の場合はNaNに
    df_access.loc[:, "duration_2"] = df_access.loc[:, "duration_2"].map(
        lambda x: "" if x is None else x
    )
    df_access.loc[
        (
            df_access["duration_2"].str.contains("バス")
            | df_access["duration_2"].str.contains("車")
        ),
        ["line_2", "station_2", "duration_2"],
    ] = ["", "", ""]
    df_access.loc[:, "station_2"] = df_access["station_2"].str.replace("駅", "")
    df_access.loc[:, "duration_2"] = (
        df_access["duration_2"]
        .map(lambda x: np.nan if x == "" else x.replace("徒歩", "").replace("分", ""))
        .astype(float)
    )

    # 3つめの最寄り駅がバス/車の場合はNaNに
    df_access.loc[:, "duration_3"] = df_access.loc[:, "duration_3"].map(
        lambda x: "" if x is None else x
    )
    df_access.loc[
        (
            df_access["duration_3"].str.contains("バス")
            | df_access["duration_3"].str.contains("車")
        ),
        ["line_3", "station_3", "duration_3"],
    ] = ["", "", ""]
    df_access.loc[:, "station_3"] = df_access["station_3"].str.replace("駅", "")
    df_access.loc[:, "duration_3"] = (
        df_access["duration_3"]
        .map(lambda x: np.nan if x == "" else x.replace("徒歩", "").replace("分", ""))
        .astype(float)
    )

    # 徒歩30分以上の場合は30分とする
    df_access.loc[df_access.duration_1 > 30, "duration_1"] = 30
    df_access.loc[df_access.duration_2 > 30, "duration_2"] = 30
    df_access.loc[df_access.duration_3 > 30, "duration_3"] = 30

    df = pd.concat([df, df_access], axis=1)
    return df


# 階建, 階
def pre_kai(df):
    def floor_map(x):

        if type(x) == float:
            return x

        elif "／" not in x:
            if "階建" in x:
                return np.nan

            else:
                float(x.replace("階", ""))

        else:
            if x.split("／")[0] == "":
                return np.nan
            elif "地下" in x.split("／")[0]:
                return float(x.split("／")[0].replace("階", "").replace("地下", "-"))
            else:
                return float(x.split("／")[0].replace("階", ""))

    def stories(x):
        if type(x) == float:
            return x

        elif len(x.split("／")) == 2 and x.split("／")[0] != "" and x.split("／") != "":
            return float(
                x.split("／")[1].replace("（", "(").split("(地下")[0].replace("階建", "")
            )

    df.loc[:, "floor"] = df["所在階"].map(floor_map)
    df.loc[:, "stories"] = df["所在階"].map(stories)
    return df


# preprocessing
def preprocessing(df):
    df = rename_cols(df)
    df = pre_area(df)
    df = pre_ward(df)
    df = pre_direction(df)
    df = pre_madori(df)
    df = pre_contract_period(df)
    df = pre_access(df)
    df = pre_kai(df)
    df = pre_kitchen(df)
    df = pre_bath(df)
    df = pre_comm(df)
    df = pre_room_equip(df)
    return df


# Feature Engineering

# Floor relative
def fe_floor_relative(df):
    df.loc[:, "floor_relative"] = df["floor"] / df["stories"]
    return df


def feature_engineering(df):
    df = fe_floor_relative(df)
    return df


# In[9]:


# Categorical encoding

# Use the number of feature as a feature
def fe_count_all(df_train, df_test, cat_features=None):
    for col in cat_features:
        df_train[col + "_countall"] = df_train[col].map(
            pd.concat([df_train[col], df_test[col]], ignore_index=True).value_counts(
                dropna=False
            )
        )
        df_test[col + "_countall"] = df_test[col].map(
            pd.concat([df_train[col], df_test[col]], ignore_index=True).value_counts(
                dropna=False
            )
        )
    return df_train, df_test


# Categorical Encoding
def categorical_encoding(df, cat_features):
    for col_name in cat_features:
        df[col_name + "_cat"] = df[col_name].astype("category").cat.codes
    return df


def dummy_cat_encoding(df, cat_features):
    for col in cat_features:
        t = pd.get_dummies(df[col])
        t.columns = col + "_" + t.columns
        df = pd.concat([df, t], axis=1)
        df = df.drop(col, axis=1)
    return df


# Read the data
df_train = pd.read_csv("input/train.csv")
df_test = pd.read_csv("input/test.csv")

# Preprocessing
df_train = preprocessing(df_train)
df_test = preprocessing(df_test)

# Feature Engineering
df_train = feature_engineering(df_train)
df_test = feature_engineering(df_test)

cat_features = [
    "ward",
    #     "ward_detail",
    "line_1",
    #     "station_1",
    "line_2",
    #     "station_2",
    #     "line_3",
    #     "station_3",
    "madori",
    "direction",
]

# Count encoding
df_train, df_test = fe_count_all(df_train, df_test, cat_features)

# Simple Categorical Encoding
df_train = dummy_cat_encoding(df_train, cat_features)
df_test = dummy_cat_encoding(df_test, cat_features)

df = pd.concat([df_train, df_test], axis=0, sort=True)


# Fill NaN
fill_na_cols = [
    "duration_1",
    "duration_2",
    "duration_3",
    "floor",
    "stories",
    "floor_relative",
    "contract_period",
    "teiki_shakuya",
]
for col in fill_na_cols:
    df_train.loc[:, col] = df_train[col].fillna(-1)
    df_test.loc[:, col] = df_test[col].fillna(-1)


# ### TODO
# * 駅徒歩時間を最大値、最小値、平均値、駅の個数に分ける
# * 間取りを連続的な数値に
# * 最寄り駅の緯度経度
# Drop columns
drop_cols = [
    "アクセス",
    "キッチン",
    "バス・トイレ",
    "周辺環境",
    "契約期間",
    "室内設備",
    "建物構造",
    "所在地",
    "所在階",
    "放送・通信",
    "方角",
    "築年数",
    "間取り",
    "面積",
    "駐車場",
    #     "direction",
    #     "line_1",
    "station_1",
    #     "line_2",
    "station_2",
    "line_3",
    "station_3",
    #     "ward",
    "ward_detail",
    #     "madori",
    "id",
]

train = df_train.drop(drop_cols, axis=1, inplace=False)
test = df_test.drop(drop_cols, axis=1, inplace=False)

train.to_csv("data/example_train.csv")
test.to_csv("data/example_test.csv")
