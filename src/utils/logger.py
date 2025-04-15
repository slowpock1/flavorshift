import logging
import os

def setup_logging():
    os.makedirs("src/logs", exist_ok=True)
    logging.basicConfig(
        filename="src/logs/migration.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Starting...")