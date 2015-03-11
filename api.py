from flask import Flask
from flask.ext import restful
from flask_cors import CORS

from config import settings

SENDHUB_API = Flask(__name__)
CORS_FASTLANE = CORS(SENDHUB_API)


if settings.DEBUG:
    SENDHUB_API.debug = True

FASTLANE_API = restful.Api(SENDHUB_API)

from endpoints import ALL_ENDPOINTS

for endpoint in ALL_ENDPOINTS:
    FASTLANE_API.add_resource(endpoint, '/api/' + settings.BASE_API_VERSION + endpoint.location)

if __name__ == '__main__':
    SENDHUB_API.run(port=5000)