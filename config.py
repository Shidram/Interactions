import os

class Config:
    # General Config
    SECRET_KEY = os.urandom(12)
    DEBUG = True
    #db Config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///employees.sqlite3"
    