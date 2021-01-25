from flask_migrate import MigrateCommand

from app import app
from flask_script import Manager, Server

current_app = app.create_app()
manager = Manager(current_app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='192.168.0.104', port=5000))
if __name__ == '__main__':
    manager.run()
