import os

base_path = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY='thisisasupersecretkey'
    DEBUG=False
    TESTING=False

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass

create_config = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)