from flask import Flask
from routes.pessoa_routes import pessoa_bp

app = Flask(__name__)
app.register_blueprint(pessoa_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
