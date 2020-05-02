import os

base_path = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY='thisisasupersecretkey'
    DEBUG=False
    TESTING=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:////' + os.path.join(base_path, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestingConfig(Config):
    DEBUG = True
    TESTING=True
    WTF_CSRF_ENABLED=False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:////' + os.path.join(base_path, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

create_config = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)