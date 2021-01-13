from app.extension import db


class DestinationExtension(db.Model):
    __tablename__ = "destination_extension"
    id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.Integer)
    rate = db.Column(db.Integer)
    views = db.Column(db.Integer)
