import os
import sys
from pathlib import Path

PROJECT_DIR = os.getcwd()
INPUT_FILE_PATH = Path("../..")
sys.path.insert(0, PROJECT_DIR)


# settings
EXP_ID = "exp4"
DATA_DIR = "../../input"
SEED = 42
ID_COLUMNS = "id"
TARGET_COLUMNS = ["target"]
N_CLASSES = len(TARGET_COLUMNS)
N_FOLDS = 5  # n_folds for Cross-Validation
