import logging
from pathlib import Path


ROOT_DIR=Path(__file__).resolve().parent.parent
LOG_DIR=ROOT_DIR/"logs"
LOG_DIR.mkdir(exist_ok=True) 


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR/"monitor.log"),
    ],
)

