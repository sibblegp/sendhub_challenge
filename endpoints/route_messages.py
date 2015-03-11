__author__ = 'gsibble'

from _base_endpoint import ApiEndpoint
from flask_restful import reqparse

import phonenumbers

from helpers.routing_logic import determine_routes, determine_ips_for_routes

class RouteMessages(ApiEndpoint):
    location = '/messages/route'

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('message', required=True, type=str)
    post_parser.add_argument('recipients', required=True, action='append')

    def post(self):
        post_arguments = self.post_parser.parse_args()

        all_phone_numbers_valid = True
        invalid_number = None
        recipients = post_arguments.get('recipients')
        if len(recipients) > 5000:
            self.make_response({'error': 'Too many recipients', 'recipient count': len(recipients)})
        for recipient in recipients:
            try:
                number = phonenumbers.parse(recipient)
            except phonenumbers.NumberParseException:
                return self.make_response({'error': 'Unable to parse phone number', 'invalid number': recipient}, 400)
            if phonenumbers.is_valid_number(number) == False:
                all_phone_numbers_valid = False
                invalid_number = recipient

            if number.country_code != 1:
                all_phone_numbers_valid = False
                invalid_number = recipient


            if all_phone_numbers_valid == False:
                return self.make_response({'error': 'Invalid Number detected', 'invalid_number': invalid_number}, 400)

        sorted_recipients = determine_routes(post_arguments['recipients'])
        assigned_ips = determine_ips_for_routes(sorted_recipients)

        return self.make_response(assigned_ips, 200)