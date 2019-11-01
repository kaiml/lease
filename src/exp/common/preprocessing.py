import os
import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = os.getcwd()
INPUT_FILE_PATH = Path("../..")
sys.path.insert(0, PROJECT_DIR)

from src.preprocess.main import pp  # isort:skip # noqa: E402


def preprocessing(df):
    df = pp(df)

    # fill NaN with most frequent values
    df.loc[:, "direction"] = df["direction"].fillna(
        df["direction"].value_counts().index[0]
    )
    df.loc[:, "material"] = df["material"].fillna(
        df["material"].value_counts().index[0]
    )
    df.loc[:, "layout"] = df["layout"].fillna(df["layout"].value_counts().index[0])
    df.loc[:, "address_1"] = df["address_1"].fillna(
        df["address_1"].value_counts().index[0]
    )

    # One-Hot Encoding
    df = pd.concat(
        [df, pd.get_dummies(df["direction"], prefix="ohe_direction")], axis=1
    )
    df = pd.concat([df, pd.get_dummies(df["layout"], prefix="ohe_layout")], axis=1)
    df = pd.concat([df, pd.get_dummies(df["material"], prefix="ohe_material")], axis=1)
    df = pd.concat([df, pd.get_dummies(df["address_1"], prefix="ohe_address1")], axis=1)

    # Drop unused columns
    df = df.drop(
        [
            "id",
            "age",
            "age_month",
            "layout",
            "material",
            "direction",
            "neighbor",
            "address_1",
            "line_1",
            "station_1",
            "duration_1",
            "line_2",
            "station_2",
            "duration_2",
            "is_bus_2",
            "line_3",
            "station_3",
            "duration_3",
            "is_bus_3",
            "address_2",
            "address_3",
        ],
        axis=1,
    )

    return df
