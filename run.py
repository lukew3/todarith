from flask import Flask
from todarith import create_app
#from todarith.config import config

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="localhost")
