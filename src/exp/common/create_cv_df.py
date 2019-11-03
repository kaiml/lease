import pandas as pd
from sklearn.model_selection import StratifiedKFold


def create_cv_df(n_splits=5, random_state=42, train_df=pd.DataFrame()):
    cv_df = pd.DataFrame()
    y = train_df["target"].values

    folds = StratifiedKFold(
        n_splits=n_splits, shuffle=True, random_state=random_state
    ).split(train_df, y)
    for n_fold, (train_index, val_index) in enumerate(folds):
        df = train_df.copy()
        df.loc[train_index, "data_type"] = "train"
        df.loc[val_index, "data_type"] = "val"
        df.loc[:, "n_fold"] = n_fold
        cv_df = pd.concat([cv_df, df.reset_index()])

    return cv_df
