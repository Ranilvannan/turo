class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/turo?user=kivy&password=kivy@123"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CUSTOM_STATIC_PATH = "/home/kivy/Desktop/images/"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
