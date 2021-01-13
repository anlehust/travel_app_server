from sqlalchemy_filters import apply_filters
from app.extension import db
from database.Destination import Destination
from database.DestinationExtension import DestinationExtension

class DestinationController:
    def get_destination_by_id(self, destination_id):
        query = db.session.query(Destination)
        condition = [
            {'field': 'id', 'op': '==', 'value': destination_id}
        ]
        des = apply_filters(query, condition).first();
        print(des.address)
