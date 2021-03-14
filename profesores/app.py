from flask import Flask
from sqlalchemy import event, engine
from sqlalchemy.schema import CreateSchema

from api import profesores_api
import models

app = Flask(__name__)
app.register_blueprint(profesores_api)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:1234@profesor_db:5432/postgres',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
))

models.init_app(app)
models.create_tables(app)


@app.route('/')
def hello_world():
    return 'Hello Profesores!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
