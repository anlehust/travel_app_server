from flask_migrate import MigrateCommand, Migrate

from app import app
from flask_script import Manager

from app.extension import db

current_app = app.create_app()
manager = Manager(current_app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
