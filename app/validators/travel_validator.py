from marshmallow import Schema, fields

class TravelCreateValidator(Schema):
    user_id = fields.Str(required=True)
    from_ = fields.Dict(
        keys=fields.Str(),
        values=fields.Float(),
        required=True
    )
    to = fields.Dict(
        keys=fields.Str(),
        values=fields.Float(),
        required=True
    )

class TravelUpdateValidator(Schema):
    user_id = fields.Str()
    from_ = fields.Dict(
        keys=fields.Str(),
        values=fields.Float(),
    )
    to = fields.Dict(
        keys=fields.Str(),
        values=fields.Float(),
    )