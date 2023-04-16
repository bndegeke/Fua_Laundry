from flask import Flask
from flask_migrate import Migrate
from .models import db  , User
from flask_login import LoginManager


# import the apps configuration
from .config import Config



migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.signin"



def create_app():
    app = Flask(__name__)
    # Load the configuration class
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app , db)
    login_manager.init_app(app)



    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    from app.routes.home import home
    app.register_blueprint(home)


    from app.routes.gallery import gallery
    app.register_blueprint(gallery)


    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.booking import booking
    app.register_blueprint(booking)

    return app