from flask import Flask, request, make_response

from src.controller.controller import *


def main():
    controller = Controller()
    controller.create_database()

    app = Flask(__name__)
    define_routes(app)
    app.run(debug=True, host="0.0.0.0")


def define_routes(app):
    @app.route('/')
    def index():
        return "<p>/accounts para retornar as contas</p>" \
               "<p>/entries para retornar as entradas</p>"

    @app.route('/isidro')
    def fun():
        return "<p>/conhaquinho</p>"

    @app.route('/accounts')
    def all_accounts():
        controller = Controller()
        accounts = controller.get_all_accounts()
        accounts = {'accounts': list(map((lambda account: account.__dict__()), accounts))}
        return accounts

    @app.route('/accounts/<account_id>')
    def get_account(account_id):
        controller = Controller()
        account = controller.get_account(account_id)
        if account is not None:
            return account.__dict__()
        return make_response({'status': 404, 'error': 'not found', 'message': 'account not found'}, 404)

    @app.route('/accounts', methods=['POST'])
    def add_account():
        name = request.form['name']
        account_type = request.form['type']
        color = request.form['color']
        controller = Controller()
        created_account = controller.create_account(name, account_type, color)
        if created_account is not None:
            account_dict = created_account.__dict__()
            return make_response(account_dict, 201)
        return make_response({'status': 400, 'error': 'bad request', 'message': 'could not create account'}, 400)

    @app.route('/entries')
    def all_entries():
        controller = Controller()
        entries = controller.get_all_entries()
        entries = {'entries': list(map((lambda entry: entry.__dict__()), entries))}
        return entries


main()
