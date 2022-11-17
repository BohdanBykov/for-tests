import os
from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    # test page
    @app.route('/')
    def test():
        return app.config['DBHOST']

    from . import db
    db.init_app(app)

    # with app.app_context():
    #     db.get_db()

    return app
