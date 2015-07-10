import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = ""
    DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
