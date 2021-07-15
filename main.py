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
        return accounts

    @app.route('/accounts/<account_id>')
    def get_account_details(account_id):
        account = get_account(account_id)
        if account is not None:
            return account.__dict__()
        return make_response({'status': 404, 'error': 'not found', 'message': 'account not found'}, 404)

    @app.route('/accounts/<account_id>/entries')
    def get_account_entries(account_id):
        entries = get_entries_by_account(account_id)
        if entries is not None:
            return {'entries': list(map((lambda entry: entry.__dict__()), entries))}
        return make_response({'status': 404, 'error': 'not found', 'message': 'account not found'}, 404)

    @app.route('/accounts', methods=['POST'])
    def add_account():
        name = request.form['name']
        account_type = request.form['type']
        color = request.form['color']

        created_account = create_account(name, account_type, color)
        if created_account is not None:
            account_dict = created_account.__dict__()
            return make_response(account_dict, 201)
        return make_response({'status': 400, 'error': 'bad request', 'message': 'could not create account'}, 400)

    @app.route('/entries')
    def all_entries():
        entries = get_all_entries()
        entries = {'entries': list(map((lambda entry: entry.__dict__()), entries))}
        return entries

    @app.route('/entries', methods=['POST'])
    def add_entry():
        account_id = int(request.form['account_id'])
        date = request.form['date']
        category = request.form['category']
        value = int(request.form['value'])
        description = request.form['description']
        commentary = request.form['commentary']

        created_entry = create_entry(account_id, date, category, value, description, commentary)
        if created_entry is not None:
            account_dict = created_entry.__dict__()
            return make_response(account_dict, 201)
        return make_response({'status': 400, 'error': 'bad request', 'message': 'could not create account'}, 400)


main()
