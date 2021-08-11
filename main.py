from flask import Flask, request, make_response
from src.controller.controller import *


def main():
    create_database()

    app = Flask(__name__)
    define_routes(app)
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0")  # Opens server to whole network


def define_routes(app):
    @app.route('/')
    def index():
        return """<h3>My Finances</h3>
                  <h4>Help</h4>
                  <ul>
                  <li>GET - <code>/accounts</code> - Lists all accounts</li>
                  <li>GET - <code>/accounts/&lt;id&gt;</code> - Lists specific account</li>
                  <li>POST - <code>/accounts</code> - Creates a new account</li>
                  <li>GET - <code>/entries</code> - Lists all entries</li>
                  </ul>"""

    @app.route('/accounts')
    def all_accounts():
        accounts = get_all_accounts()
        accounts = {'accounts': list(map((lambda account: account.__dict__()), accounts))}
        print(accounts)
        return accounts

    @app.route('/accounts/<account_id>')
    def get_account_details(account_id):
        account = get_account(account_id)

        if account is not None:
            response = account.__dict__()
            print(response)
            return response

        response = {'status': 404, 'error': 'not found', 'message': 'account not found'}
        print(response)
        return make_response(response, 404)

    @app.route('/accounts/<account_id>/entries')
    def get_account_entries(account_id):
        entries = get_entries_by_account(account_id)

        if entries is not None:
            response = {'entries': list(map((lambda entry: entry.__dict__()), entries))}
            print(response)
            return response

        response = {'status': 404, 'error': 'not found', 'message': 'account not found'}
        print(response)
        return make_response(response, 404)

    @app.route('/accounts', methods=['POST'])
    def add_account():
        if request.is_json:
            content = request.get_json()
        else:
            content = request.form

        name = content['name']
        account_type = content['type']
        color = content['color']

        created_account = create_account(name, account_type, color)
        if created_account is not None:
            response = created_account.__dict__()
            print(response)
            return make_response(response, 201)

        response = {'status': 400, 'error': 'bad request', 'message': 'could not create account'}
        print(response)
        return make_response(response, 400)

    @app.route('/entries')
    def all_entries():
        entries = get_all_entries()
        response = {'entries': list(map((lambda entry: entry.__dict__()), entries))}
        print(response)
        return response

    @app.route('/entries/<entry_id>')
    def get_entry_details(entry_id):
        entry = get_entry(entry_id)

        if entry is not None:
            response = entry.__dict__()
            print(response)
            return response

        response = {'status': 404, 'error': 'not found', 'message': 'entry not found'}
        print(response)
        return make_response(response, 404)

    @app.route('/entries', methods=['POST'])
    def add_entry():
        if request.is_json:
            content = request.get_json()
        else:
            content = request.form

        account_id = int(content['account_id'])
        date = content['date']
        category = content['category']
        value = int(content['value'])
        description = content['description']
        commentary = content['commentary']

        created_entry = create_entry(account_id, date, category, value, description, commentary)

        if created_entry is not None:
            response = created_entry.__dict__()
            print(response)
            return make_response(response, 201)

        response = {'status': 400, 'error': 'bad request', 'message': 'could not create account'}
        print(response)
        return make_response(response, 400)


main()
