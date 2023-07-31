from flask import Flask
from app.api import bp as api_bp
from app.models import db
from scheduler import run_scheduler

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()
        run_scheduler()  # Run the scheduler when the app starts

    return app
