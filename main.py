from flask import Flask, request, make_response
from flask_cors import cross_origin
from src.controller.controller import *
from src.util.MessageLog import log_request, log_response
from src.util.FieldGetter import *


def main():
    create_database()

    app = Flask(__name__)
    define_routes(app)
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0")  # Opens server to whole network


def define_routes(app):
    @app.route('/accounts')
    @cross_origin()
    def all_accounts():
        log_request(request.path)

        accounts = get_all_accounts()
        response = {'accounts': list(map((lambda account: account.__dict__()), accounts))}

        log_response(response)

        return response

    @app.route('/accounts/<account_id>')
    @cross_origin()
    def get_account_details(account_id):
        log_request(request.path)

        account = get_account(account_id)
        if account is not None:
            response = account.__dict__()
            log_response(response)
            return response

        response = {'status': 404, 'error': 'not found', 'message': 'account not found'}
        log_response(response)
        return make_response(response, 404)

    @app.route('/accounts/<account_id>/entries')
    @cross_origin()
    def get_account_entries(account_id):
        log_request(request.path)

        entries = get_entries_by_account(account_id)

        if entries is not None:
            response = {'entries': list(map((lambda entry: entry.__dict__()), entries))}
            log_response(response)
            return response

        response = {'status': 404, 'error': 'not found', 'message': 'account not found'}
        log_response(response)
        return make_response(response, 404)

    @app.route('/accounts', methods=['POST'])
    @cross_origin()
    def add_account():
        if request.is_json:
            content = request.get_json()
        else:
            content = request.form

        log_request(request.path, content)

        name = content['name']
        account_type = content['type']
        color = content['color']

        created_account = create_account(name, account_type, color)
        if created_account is not None:
            response = created_account.__dict__()
            log_response(response)
            return make_response(response, 201)

        response = {'status': 400, 'error': 'bad request', 'message': 'could not create account'}
        log_response(response)
        return make_response(response, 400)

    @app.route('/entries')
    @cross_origin()
    def all_entries():
        log_request(request.path)

        entries = get_all_entries()
        response = {'entries': list(map((lambda entry: entry.__dict__()), entries))}

        log_response(response)

        return response

    @app.route('/entries/<entry_id>')
    @cross_origin()
    def get_entry_details(entry_id):
        log_request(request.path)

        entry = get_entry(entry_id)
        if entry is not None:
            response = entry.__dict__()
            log_response(response)
            return response

        response = {'status': 404, 'error': 'not found', 'message': 'entry not found'}
        log_response(response)
        return make_response(response, 404)

    @app.route('/entries', methods=['POST'])
    @cross_origin()
    def add_entry():
        if request.is_json:
            content = request.get_json()
        else:
            content = request.form

        log_request(request.path, content)

        try:
            origin_account_id = get_field(content, 'origin_account_id', required=True, is_number=True)
            destiny_account_id = get_field(content, 'destiny_account_id', required=False, is_number=True)
            date = get_field(content, 'date', required=True)
            category = get_field(content, 'category', required=True)
            value = get_field(content, 'value', required=True, is_number=True)
            description = get_field(content, 'description', required=False)
            commentary = get_field(content, 'commentary', required=False)
        except KeyError as exception:
            response = {'status': 400, 'error': 'bad request', 'message': exception}
            log_response(response)
            return make_response(response, 400)

        created_entry = create_entry(origin_account_id, destiny_account_id, date,
                                     category, value, description, commentary)
        if created_entry is not None:
            response = created_entry.__dict__()
            log_response(response)
            return make_response(response, 201)

        response = {'status': 400, 'error': 'bad request', 'message': 'could not create account'}
        log_response(response)
        return make_response(response, 400)


main()
