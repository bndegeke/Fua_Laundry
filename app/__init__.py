from flask import Flask
from flask_migrate import Migrate
from .models import db , login_manager


# import the apps configuration
from .config import Config



migrate = Migrate()




def create_app():
    app = Flask(__name__)
    # Load the configuration class
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app , db)
    login_manager.init_app(app)


    from app.routes.home import home
    app.register_blueprint(home)


    from app.routes.gallery import gallery
    app.register_blueprint(gallery)


    from app.routes.auth import auth
    app.register_blueprint(auth)

    return app