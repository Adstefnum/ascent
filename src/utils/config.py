import os
from dotenv import load_dotenv
load_dotenv()


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:%(filename)s:%(lineno)04d:%(message)s')  # :%(funcName)s
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)



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