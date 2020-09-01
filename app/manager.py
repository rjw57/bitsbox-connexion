from flask_migrate import MigrateCommand
from flask_script import Manager

from .app import application

manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    import app  # required to make sure all the models are registered  # noqa: F401
    manager.run()
