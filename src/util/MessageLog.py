import json


def log_request(path, request=""):
    print("REQUEST MESSAGE:")
    print(path)
    if request != "":
        log_message(request)


def log_response(response):
    print("RESPONSE MESSAGE:")
    log_message(response)


def log_message(message):
    parsed_message = message
    print(json.dumps(parsed_message, indent=4))
