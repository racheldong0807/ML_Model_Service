
from marshmallow import Schema, fields



class ModelResponseSchema(Schema):
    model_id = fields.Str(required=True)
    result = fields.Dict()

class ModelInfoResponseSchema(Schema):
    model_id = fields.Str(required=True)
    name = fields.Str()
    last_training_timestamp = fields.Str()
    complete = fields.Boolean()