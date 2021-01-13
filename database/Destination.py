from app.extension import db


class Destination(db.Model):
    __tablename__ = "destination"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
