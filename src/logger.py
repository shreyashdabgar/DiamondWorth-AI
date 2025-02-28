import logging
import os
from datetime import datetime

# Generate a log file becuase we put there .log name based on the current date in the format 'YYYY-MM-DD.log' and store it in the LOG_FILE variable
LOG_FILE = datetime.now().strftime('%Y-%m-%d') + '.log' 
# Create the logs directory path by joining the current working directory with 'logs' and the generated log file name
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d',
    level=logging.INFO
)

