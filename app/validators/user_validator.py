from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

class UserCreateValidator(Schema):
    name = fields.Str(required=True, validate=Length(max=60))
    age = fields.Integer(required=True, validate=Range(min=18, max=100))
    driver_license_type = fields.Str(required=True, validate=Length(max=5))
    is_busy = fields.Bool(required=True)
    has_vehicle = fields.Bool(required=True)
    vehicle_type_id = fields.Integer(required=True)

class UserUpdateValidator(Schema):
    name = fields.Str(validate=Length(max=60))
    age = fields.Integer(validate=Range(min=18, max=100))
    driver_license_type = fields.Str(validate=Length(max=5))
    is_busy = fields.Bool()
    has_vehicle = fields.Bool()
    vehicle_type_id = fields.Integer()