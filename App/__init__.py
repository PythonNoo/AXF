from flask import Flask

from App.ext import init_ext


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = '110'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rock1204@localhost:3306/AXF_GitHub'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_ext(app)

    init_urls(app)

    return app