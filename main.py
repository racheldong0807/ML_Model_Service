#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Xin Lu Dong
# @Contact: dongxinlu@neusoft.edu.cn
from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from ml_model_service.controller import (
 ModelInfo, 
 ModelInference, 
 ModelTraining,
)

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app,
                  config={"title": "ML Model Service",
                            "version": "1.0.0",
                            "swagger_ui": True,
                            "description": "ML Model Service API",},
                  merge=True)

api.add_resource(ModelInfo, '/info/')
api.add_resource(ModelInference, '/infer/')
api.add_resource(ModelTraining, '/train/')


if __name__ == '__main__':
    app.run(debug=True)

