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
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:dynamo@localhost/dynamo'
    DEBUG =True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}