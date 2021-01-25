from flask import Blueprint, jsonify

from controller.destination import DestinationController
from schema.destination import DestinationSchema

destination = Blueprint('destination', __name__)
destination_controller = DestinationController()

destination_schema = DestinationSchema()

@destination.route('/')
def get_by_id():
    res = destination_controller.get_destination_by_id(1)
    return destination_schema.dump(res)

@destination.route('/des')
def get_all():
    res = destination_controller.get_all_destination()
    return destination_schema.dumps(res, many=True)

