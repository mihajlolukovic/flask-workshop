from jproperties import Properties

from app import create_app

# Gunicorn entry point
application = create_app()

# Read application properties
configs = Properties()

with open('application.properties', 'rb') as config_file:
    configs.load(config_file)

if __name__ == '__main__':
    application.run(
        host=configs.get('server.host').data,
        port=configs.get('server.port').data,
        debug=True
    )
