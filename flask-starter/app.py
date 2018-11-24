from flask import Flask
import config
from models import db
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
app.debug = config.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = config.SQLALCHEMY_POOL_SIZE
app.config['SQLALCHEMY_MAX_OVERFLOW'] = config.SQLALCHEMY_MAX_OVERFLOW
app.config['SECRET_KEY'] = config.SECRET_KEY

db.init_app(app)
db.app = app

jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

import routes.user

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)