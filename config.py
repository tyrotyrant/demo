import os

class Config:


    SECRET_KEY =('1234')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/events'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
