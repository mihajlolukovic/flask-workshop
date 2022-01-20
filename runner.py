import configparser
import os

from app import create_app

# Gunicorn entry point
application = create_app()

# Read application properties
dir_path = os.path.dirname(os.path.realpath('application.properties'))
file = os.path.join(dir_path, 'application.properties')
config = configparser.ConfigParser()
config.read(file)

host = config.get("Server", "host")
port = config.get("Server", "port")

if __name__ == '__main__':
    application.run(host=host, port=port, debug=True)
