import logging
import os

logging.basicConfig(
    filename=os.path.join("logs", "bot.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)