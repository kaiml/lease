import gc
import os
import sys
from pathlib import Path

PROJECT_DIR = os.getcwd()
INPUT_FILE_PATH = Path("../..")
sys.path.insert(0, PROJECT_DIR)

from src.preprocess.read_file import read_file  # isort:skip # noqa: E402


def step2_load_data(DATA_DIR):
    train_df, test_df = read_file(DATA_DIR=DATA_DIR)
    gc.collect()
    return train_df, test_df
