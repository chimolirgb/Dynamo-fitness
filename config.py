import os
class Config():
    
   
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY =os.environ.get("SECRET_KEY")
    #Simplemde configuration
   
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    #photos destinations
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    

class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ephraim:junior54@localhost/eph'
    DEBUG =True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}