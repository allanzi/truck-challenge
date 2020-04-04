from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

class TerminalCreateValidator(Schema):
    user_id = fields.Str(required=True)
    is_busy = fields.Bool(required=True)
