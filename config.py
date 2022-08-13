from distutils.debug import DEBUG
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABELED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLACHEMY_DATABASE_URI = os.environ['DATABSE_URL']
    
    
class ProductionConfig(config):
    DEBUG = False
    
    
class StagingConfig(config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(config):
    DEVELOPEMENT = True
    DEBUG = True
    
class TestingConfig(config):
    TESTING = True