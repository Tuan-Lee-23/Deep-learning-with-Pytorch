import logging
from datetime import datetime
from pytz import timezone

def timetz(*args):
    tz = timezone('Asia/Saigon')
    return datetime.now(tz).timetuple()

logging.Formatter.converter = timetz
logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    filename='failed_images.log'
)
