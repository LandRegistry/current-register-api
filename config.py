import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost/currentregister"
    DEBUG = False
    
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost/currentregister"
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
