# floor_stories : floor (int), stories(int)
def pp_floor_stories(df):
    floor = df["floor_stories"].str.split("／", expand=True).iloc[:, 0]
    stories = df["floor_stories"].str.split("／", expand=True).iloc[:, 1]

    # "xx階建"のみの場合は1階にする
    floor[floor.str.contains("階建").fillna(False)] = "1"
    floor = floor.str.replace(r"（地下\d階）", "")
    floor = floor.str.replace("地下", "-")
    floor = floor.str.replace("階", "")

    # fill 2 in case of nan
    floor[floor.isna()] = "2"
    floor[floor == ""] = "2"
    floor = floor.astype(int)

    stories = stories.str.replace(r"（地下\d階）", "").str.replace("階建", "")
    stories[(stories is None) | (stories.isna())] = 2
    stories = stories.astype(int)

    df.loc[:, "floor"] = floor
    df.loc[:, "stories"] = stories
    return df
