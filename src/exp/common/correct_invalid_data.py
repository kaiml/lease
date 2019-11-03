def correct_invalid_data(train_df):
    train_df.loc[5775, "area"] = "200m2"
    train_df.loc[20926, "area"] = "40.01m2"
    train_df.loc[train_df["target"] > 1500000, "target"] = 1500000
    return train_df
