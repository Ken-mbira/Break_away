from flask import Flask

def create_app():
    """This is the application factory
    """
    app = Flask(__name__)

    #registering the blueprint
    from .auth.v1 import main
    app.register_blueprint(main)

    return app