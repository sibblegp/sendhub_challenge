from flask import Flask
from flask.ext import restful
from flask_cors import CORS

from config import settings

SENDHUB = Flask(__name__)
CORS_FASTLANE = CORS(SENDHUB)


if settings.DEBUG:
    SENDHUB.debug = True

SENDHUB_API = restful.Api(SENDHUB)

from endpoints import ALL_ENDPOINTS

for endpoint in ALL_ENDPOINTS:
    SENDHUB_API.add_resource(endpoint, '/api/' + settings.BASE_API_VERSION + endpoint.location)

if __name__ == '__main__':
    SENDHUB.run(port=5000)