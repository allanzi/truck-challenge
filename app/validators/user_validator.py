from marshmallow import Schema, fields
from marshmallow.validate import Length

class UserValidator(Schema):
    name = fields.Str(required=True, validate=Length(max=60))