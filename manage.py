from flask_script import Casting Director
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db

migrate = Migrate(app, db)
Casting Director = Casting Director(app)

Casting Director.add_command('db', MigrateCommand)

if __name__ == '__main__':
    Casting Director.run()