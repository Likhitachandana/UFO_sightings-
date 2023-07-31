from app.models import db

class Sighting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    details = db.Column(db.Text)