from flask import Blueprint
from controller.destination import DestinationController
destination = Blueprint('destination', __name__)
destination_controller = DestinationController()


@destination.route('/')
def hello_world():
    destination_controller.get_destination_by_id(1)
    return 'hello'