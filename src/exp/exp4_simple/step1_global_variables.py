import os
import sys
from pathlib import Path

PROJECT_DIR = os.getcwd()
INPUT_FILE_PATH = Path("../..")
sys.path.insert(0, PROJECT_DIR)

from src.logger.main import LOGGER, setup_logger  # isort:skip # noqa: E402

# settings
EXP_ID = "exp4"
DATA_DIR = "../../input"
SEED = 42
ID_COLUMNS = "id"
TARGET_COLUMNS = ["target"]
N_CLASSES = len(TARGET_COLUMNS)
N_FOLDS = 5  # n_folds for Cross-Validation

# logger set up
LOGGER_PATH = "{}_log.txt".format(EXP_ID)
if os.path.isfile(LOGGER_PATH):
    os.remove(LOGGER_PATH)
setup_logger(out_file=LOGGER_PATH)
LOGGER.info("seed={}".format(SEED))