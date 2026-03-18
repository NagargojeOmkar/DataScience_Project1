import os
import sys
import logging

# Log file ka folder
LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/running_logs.log"

# Folder create karo agar exist nahi hai
os.makedirs(LOG_DIR, exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
)

# Console pe bhi logs dikhane ke liye
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)

console_handler.setFormatter(formatter)

# Root logger me add karo
logging.getLogger().addHandler(console_handler)