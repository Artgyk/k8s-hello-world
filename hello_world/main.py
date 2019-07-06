import config
from api import app
import waitress


if __name__ == '__main__':
    print("Starting application")

    waitress.serve(app, port=config.LISTEN_PORT)