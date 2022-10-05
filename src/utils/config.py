import os
from dotenv import load_dotenv
load_dotenv()
# pip3 install python-dotenv - Get and set values in your .env file in
# local and production servers

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:%(filename)s:%(lineno)04d:%(message)s')  # :%(funcName)s
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# Usage: from config import logging | https://docs.python.org/3/library/logging.html
# Usage: logging.debug(SQL) ; logging.info(SQL) - error warning

# Beanstalk
beanstalk_srvname = os.getenv("BGR_BEANSTALK_SRVNAME", 'beanstalkd-v2') 
beanstalk_srvport = os.getenv("BGR_BEANSTALK_PORT", 11300)

# MySQL Connection
dbhost = ''
dbport = 3306
dbname = ''
dbuser = ''
dbpass = 'xxxxxx'

ENCODING='utf-8-sig'

fernet_key = ""

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cdec(input: str, color: BColors) -> str:
    return color + str(input) + BColors.ENDC