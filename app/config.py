import os


class Config():
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "{db}+{drive}://{username}:{password}@{host}:{port}/{database}".format(
        db='mysql',
        drive='pymysql',
        username=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', '123456'),
        host=os.getenv('MYSQL_HOST', '127.0.0.1'),
        port=os.getenv('MYSQL_PORT', '3306'),
        database=os.getenv('MYSQL_DATABASE', 'ginger'),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig,
}
