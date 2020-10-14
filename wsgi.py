from flask import Flask
from todarith import create_app

app = create_app()

if __name__ == '__main__':
    #context = ('server.crt', 'server.key')#certificate and key files
    app.run(port=5000, host="localhost")
