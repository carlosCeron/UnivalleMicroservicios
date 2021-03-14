from flask import Flask
from api import estudiantes_api
import models

app = Flask(__name__)
app.register_blueprint(estudiantes_api)

app.config.update(dict(
    SECRET_KEY="cur50",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:1234@estudiantes_db/estudiantes',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
))

models.init_app(app)
models.create_tables(app)


@app.route('/')
def hello_world():
    return 'Hello Estudiante!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
