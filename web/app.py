from flask import Blueprint, Flask
from flask_bootstrap import Bootstrap
from frontend import frontend_blueprint

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

app.register_blueprint(frontend_blueprint)

app.run(debug=True, host='0.0.0.0', port=80)
