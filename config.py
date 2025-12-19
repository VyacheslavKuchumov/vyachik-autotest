import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL =  os.getenv('BASE_URL', "http://localhost:8080")
    USER = os.getenv('USER', "admin")
    PASSWORD = os.getenv('PASSWORD', "admin")
    DB = os.getenv('DB', "PGDEV")
    APP_NAME = os.getenv('APP_NAME', "Btk_ConfiguratorMainMenu")
    START_FORM = os.getenv('START_FORM', "gtk-ru.bitec.app.btk.Btk_Class%23List")

config = Config()