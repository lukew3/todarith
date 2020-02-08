from todarith import create_app, config

app = create_app(config.dev_config)

if __name__ == '__main__':
    app.run(debug=True)
