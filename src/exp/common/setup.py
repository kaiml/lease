import os
import sys
import time
from contextlib import contextmanager
from pathlib import Path

PROJECT_DIR = os.getcwd()
INPUT_FILE_PATH = Path("../..")
sys.path.insert(0, PROJECT_DIR)

from src.logger.main import LOGGER, setup_logger  # isort:skip # noqa: E402

# settings
DATA_DIR = "../../input"
SEED = 42
ID_COLUMNS = "id"
TARGET_COLUMNS = ["target"]
N_CLASSES = len(TARGET_COLUMNS)
N_FOLDS = 5  # n_folds for Cross-Validation

# logger set up
LOGGER_PATH = "log.txt"
setup_logger(out_file=LOGGER_PATH)
LOGGER.info("seed={}".format(SEED))

# timer set up
@contextmanager
def timer(name):
    t0 = time.time()
    yield
    LOGGER.info(
        "[{}] done in {} s".format(name, round(time.time() - t0, 2))
    )  # timer set up
