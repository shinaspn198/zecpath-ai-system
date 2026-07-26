import logging
import os


# Create logs folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")


logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_logger():

    logger = logging.getLogger("ZecpathAI")

    return logger