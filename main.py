from flask import Flask
from src.routes.routes import *


def main():
    create_database()

    app = Flask(__name__)

    define_routes(app)

    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0")  # Opens server to whole network


main()
