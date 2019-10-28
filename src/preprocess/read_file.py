import pandas as pd


def read_file(DATA_DIR="./../../input"):

    col_names = {
        "アクセス": "access",
        "キッチン": "kitchen",
        "バス・トイレ": "bathroom",
        "周辺環境": "neighbor",
        "契約期間": "contract",
        "建物構造": "material",
        "所在階": "floor_stories",
        "放送・通信": "internet",
        "方角": "direction",
        "築年数": "age",
        "賃料": "target",
        "間取り": "layout",
        "面積": "area",
        "駐車場": "parking",
        "所在地": "address",
        "室内設備": "equipment",
    }

    # Read files
    train_df = pd.read_csv(f"{DATA_DIR}/train.csv").rename(columns=col_names)
    test_df = pd.read_csv(f"{DATA_DIR}/test.csv").rename(columns=col_names)

    return train_df, test_df
