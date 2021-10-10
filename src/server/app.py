import os
import json
import traceback

from flask import Flask, request, Response, jsonify

app = Flask(__name__)



def init_module():
    """ Initializes the Flask app. """
    file = open('/data/db.json', 'r')
    DB = json.load(file)
    file.close
    print(DB)
    return DB


DB = init_module()
db_subscribe = {}

@app.route('/get', methods=['GET'])
def db_get():
    key = request.args.get('key')
    if not key:
        return {'error': 'Missing parameter \'key\''}, 400
    return {'key': key, 'value': DB.get(key)}, 200


@app.route('/set', methods=['POST'])
def db_set():
    try:
        key = request.json.get('key')
        value = request.json.get('value')
        if not key:
            return {'error': 'Missing parameter \'key\''}, 400
        if not value:
            return {'error': 'Missing parameter \'value\''}, 400
        DB[key] = value
        if key in db_subscribe.keys():
            print("SEND EMAIL")
	
        with open("/data/db.json", "w") as outfile:
            json.dump(DB, outfile)
        return {
                   'message': 'Key \'{}\' set to Value \'{}\''.format(key, value)
               }, 200
    except Exception:
        return {'error': 'Unable to process this request.'}, 422


@app.route('/remove/<key>', methods=['DELETE'])
def db_remove(key):
    try:
        if not key:
            return {'error': 'Missing parameter \'key\''}, 400
        try:
            del DB[key]
            if key in db_subscribe.keys():
                print("SEND EMAIL")

            with open("/data/db.json", "w") as outfile:
                json.dump(DB, outfile)
            return {'message': 'Key \'{}\' deleted.'.format(key)}
        except KeyError as key_err:
            return {'message': 'Key \'{}\' not found.'.format(key)}

    except Exception:
        return {
                   'error':
                       'Unable to process this request. Details: %s' %
                       traceback.format_exc(),
               }, 422


@app.route('/keys', methods=['GET'])
def db_keys():
    return {'keys': list(DB.keys())}, 200


@app.route('/values', methods=['GET'])
def db_values():
    return {'values': list(DB.values())}, 200


@app.route('/items', methods=['GET'])
def db_items():
    return {'items': [list(item) for item in DB.items()]}, 200


@app.route('/subscribe', methods=['POST'])
def key_subscribe():
    key = request.json.get('key')
    email = request.json.get('email')
    if key not in db_subscribe.keys():
        lt = []
        lt.append(email)
        db_subscribe[key] = lt
    else:
        if email in db_subscribe[key]:
            return key + " Already Subscribed by user : " + email
        else:
            val = db_subscribe[key]
            val.append(email)
            db_subscribe[key] = val
    return "Successfully Subscribed to key : " + key


@app.route('/unsubscribe', methods=['POST'])
def key_unsubscribe():
    key = request.json.get('key')
    if key not in db_subscribe.keys():
        return {'error': 'Key is not subscribe \'key\''}, 400
    else:
        del db_subscribe[key]
    return "Successfully Unsubscribed to key : " + key

@app.route('/health')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
    init_module()

