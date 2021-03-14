from datetime import datetime

import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, engine

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not engine.dialect.has_schema(engine, 'profesores'):
        engine.execute(sqlalchemy.schema.CreateSchema('profesores'))
    db.metadata.create_all(engine)
    return engine


class Profesor(db.Model):
    __table_args__ = {'schema': 'profesores'}

    id = db.Column(db.Integer, primary_key=True)
    primerNombre = db.Column(db.String(255), unique=False, nullable=False)
    segundoNombre = db.Column(db.String(255), unique=False, nullable=True)
    primerApellido = db.Column(db.String(255), unique=False, nullable=False)
    segundoApellido = db.Column(db.String(255), unique=False, nullable=False)
    profesion = db.Column(db.String(255), unique=False, nullable=False)
    correo = db.Column(db.String(255), unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def get_id(self):
        return self.id

    def to_json(self):
        return {
            'id': self.id,
            'primer_nombre': self.primerNombre,
            'segundo_nombre': self.segundoNombre,
            'primer_apellido': self.primerApellido,
            'profesion':self.profesion,
            'segundo_apellido': self.segundoApellido,
            'correo': self.correo
        }
