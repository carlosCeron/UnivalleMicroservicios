from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    return engine


class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_estudiante = db.Column(db.String(255), unique=True, nullable=False)
    direccion = db.Column(db.String(655), unique=False, nullable=True)
    telefono = db.Column(db.String(255), unique=False, nullable=False)
    identificacion = db.Column(db.String(255), unique=False, nullable=False)
    sede = db.Column(db.String(255), unique=False, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def get_id(self):
        return self.id

    def to_json(self):
        return {
            'id': self.id,
            'nombre_estudiante': self.nombre_estudiante,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'identificacion': self.identificacion,
            'sede': self.sede
        }
