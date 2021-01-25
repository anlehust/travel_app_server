
from marshmallow import Schema, fields


class DestinationSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    address = fields.String()
