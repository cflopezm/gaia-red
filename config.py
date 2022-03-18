from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MariadbUser']
password = os.environ['MariadbPass']
host = os.environ['MariadbHost']
database = os.environ['MariadbName']