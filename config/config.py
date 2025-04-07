import os
from pathlib import Path
from typing import Optional, Tuple

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Api configuration
OPENSKY_USERNAME = os.getenv("OPENSKY_USERNAME")
OPENSKY_PASSWORD = os.getenv("OPENSKY_PASSWORD")
OPENSKY_API_BASE_URL = os.getenv(
    "OPENSKY_API_BASE_URL", "https://opensky-network.org/api"
)

# Geographic bounding box for data collection
BOUNDING_BOX_STR = os.getenv("BOUNDING_BOX")
BOUNDING_BOX: Optional[Tuple[float, float, float, float]] = None
if BOUNDING_BOX_STR:
    try:
        min_lat, max_lat, min_lon, max_lon = map(
            float, BOUNDING_BOX_STR.split(",")
        )  # noqa: E501
        BOUNDING_BOX = (min_lat, max_lat, min_lon, max_lon)
    except (ValueError, TypeError):
        print(
            "Warning: Invalid BOUNDING_BOX format."
            " Should be 'min_lat,max_lat,min_lon,max_lon'"
        )

# Database Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "flight_tracker")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


# Storage Configuration
RAW_DATA_PATH = Path(os.getenv("RAW_DATA_PATH", "./data/raw"))
PROCESSED_DATA_PATH = Path(
    os.getenv("PROCESSED_DATA_PATH", "./data/processed")
)  # noqa: E501

# Prefect Configuration
PREFECT_API_KEY = os.getenv("PREFECT_API_KEY")
PREFECT_API_URL = os.getenv("PREFECT_API_URL")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = os.getenv("LOG_FORMAT", "json")

# Database URL for SQLAlchemy
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@" f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)  # noqa: E501
# Ensure data directories exist
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)
