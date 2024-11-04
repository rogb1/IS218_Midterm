import logging
import logging.config
import os

os.makedirs('logs', exist_ok=True)

LOG_CONFIG_FILE = 'logging.conf' 
logging.config.fileConfig(LOG_CONFIG_FILE)

logger = logging.getLogger()

logger.info("Application started.")
