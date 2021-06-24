from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap = Bootstrap()
db=SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'
simple = SimpleMDE()
photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)


    app.config.from_object(config_options[config_name])


    #initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    
     # configure UploadSet
    configure_uploads(app,photos)




    # register Blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint) 
    

    



    return app
