from flask_script import Server, Manager
from uwsgi import app


manager = Manager(app)
manager.add_command(
    'runserver',
    Server(port=5000, use_debugger=True, use_reloader=True))


if __name__ == '__main__':
    manager.run()
