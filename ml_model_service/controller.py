from flask_restful import Resource
from flask import request

from ml_model_service.schema import ModelResponseSchema, ModelInfoResponseSchema
 
class ModelInfo(Resource):
    def get(self):
        """
        Get the model information and training status.
        ---
        parameters:
          - name: model_id
            in: query
            description: The unique model id.
            type: string
            example: meta-llama/Llama-2-7b
        responses:
          200:
            description: The model information and the training status.
            schema:
              $ref: '#/definitions/ModelInfoResponse'
        definitions:
          ModelInfoResponse:
            type: object
            properties:
              model_id:
                type: string
                description: The unique model id.
                example: meta-llama/Llama-2-7b
              name:
                type: string
                description: The model normal name.
                example: Llama-2-7b
              last_training_timestamp:
                type: string
                format: date-time
                example: 2024-04-22T06:27:41.981Z
              complete:
                type: boolean
                description: Indicate whether the model training is finished.
                example: true
        """
        model_id = request.args.get('model_id')
        # Query data from DB
        query_result = {"model_id": model_id,
                        "name": "llm",
                        "last_training_timestamp": "2024-04-22T06:27:41.981Z",
                        "complete": False}     
        # Serialize response
        model_info_response_schema = ModelInfoResponseSchema()
        return model_info_response_schema.dump(query_result), 200


class ModelInference(Resource):
    def post(self):
        """
        Get the model inference result.
        ---
        parameters: 
          - in: body
            name: body
            required: True
            schema:
              $ref: '#/definitions/ModelRequest'
        responses:
          200:
            description: The inference result from the model.
            schema:
              $ref: '#/definitions/ModelResponse'     
        definitions:
          ModelRequest:
            type: object
            properties:
              model_id:
                type: string
                description: The unique model id.
                example: meta-llama/Llama-2-7b
              model_parameters:
                type: object
                description: The parameters to send to the model.
                example: {"temperature": 0.6, "max_tokens": 500}
          ModelResponse:
            type: object
            properties:
              model_id:
                type: string
                description: The unique model id.
                example: meta-llama/Llama-2-7b
              result:
                type: object
                description: The model output.
                example: {"generated_text": "This is an example."}
        """
        request_body = request.json
        model_id = request_body["model_id"]
        model_parameters = request_body["model_parameters"]
        # Call model
        model_response = {"model_id": model_id, 
                          "result": {"generated_text": f"This is the model output infered from given parameters: {model_parameters}"}}

        # Serialize response
        model_response_schema = ModelResponseSchema()
        return model_response_schema.dump(model_response), 200

class ModelTraining(Resource):
    def get(self):
        """
        Train or re-train the model.
        ---
        parameters:
          - name: model_id
            in: query
            description: The unique model id.
            type: string
            example: meta-llama/Llama-2-7b
        responses:
          200:
            description: Training triggered successfully.
        """
        # Train model
        return None, 200
