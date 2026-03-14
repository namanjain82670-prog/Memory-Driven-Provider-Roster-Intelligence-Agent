import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:

    # -----------------------------
    # DATA PATHS
    # -----------------------------

    ROSTER_DATA_PATH = "data/roster_processing_details.csv"
    MARKET_DATA_PATH = "data/aggregated_operational_metrics.csv"

    # -----------------------------
    # MEMORY DATABASE
    # -----------------------------

    EPISODIC_DB_PATH = "episodic_memory.db"

    # -----------------------------
    # VECTOR MEMORY SETTINGS
    # -----------------------------

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    VECTOR_INDEX_PATH = "vector_memory"

    # -----------------------------
    # ALERT THRESHOLDS
    # -----------------------------

    MARKET_SUCCESS_THRESHOLD = 85

    DURATION_ANOMALY_THRESHOLD = 2

    # -----------------------------
    # WEB SEARCH API
    # -----------------------------

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # -----------------------------
    # SYSTEM SETTINGS
    # -----------------------------

    MAX_MEMORY_RESULTS = 5

    LOGGING = True

    # -----------------------------
    # VISUALIZATION SETTINGS
    # -----------------------------

    CHART_THEME = "plotly_dark"