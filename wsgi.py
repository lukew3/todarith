from flask import Flask
from todarith import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5000, host="localhost")
