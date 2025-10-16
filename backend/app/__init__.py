import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

db = SQLAlchemy()


def create_app() -> Flask:
    load_dotenv()

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres',
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)

    from .routes import api_bp  # noqa: WPS433 (local import to avoid circular)
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.get('/health')
    def health() -> tuple[str, int]:
        return 'ok', 200

    return app


