import os
import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = os.getcwd()
INPUT_FILE_PATH = Path("../..")
sys.path.insert(0, PROJECT_DIR)

from src.preprocess.main import pp  # isort:skip # noqa: E402


def preprocessing(df=pd.DataFrame()):
    df = pp(df)

    return df
