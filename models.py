import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from setting import db_name, db_user, db_password, db_host, db_port, db_url

database_path = db_url.format(db_user, db_password, db_host, db_port, db_name)
db = SQLAlchemy()


def setup_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    with app.app_context():
        db.create_all()


class Scene(db.Model):
    __tablename__ = 'scenes'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    duration = Column(Integer())
    characters = db.relationship('Character', backref='scene',
                                 cascade="all, delete-orphan")

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'duration': self.duration
        }


class Character(db.Model):
    __tablename__ = 'characters'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    role = Column(String())
    scene_id = db.Column(db.Integer, db.ForeignKey('scenes.id'), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'scene_id': self.scene_id
        }
