import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s :: %(levelname)s :: %(message)s',
    filename="debug.log",
    filemode="w"
)

while True:
    logging.debug("loop is running")
    time.sleep(1)
