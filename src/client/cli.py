import time
import json
import requests
import optparse


def key_get(key, server):
    url = server + '/' + "get?key=" + key
    headers = {}
    response = requests.request("GET", url, headers=headers)
    return response.text


def key_set(key, value, server):
    url = server + '/' + "set"
    payload = json.dumps({
        "key": key,
        "value": value
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def key_watch(key, server):
    try:
        print('Watch started for every 5 seconds, ctrl-c to exit!')
        while 1:
            response = key_get(key, server)
            print(response)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting watch")


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-o", "--operation", dest="operation",
                      help="Choose Operation 1. set , 2. get , 3. watch")
    parser.add_option("-s", "--server", dest="server",
                      help="Please enter server along with HTTP/HTTPS , example: http://<server:port>")
    parser.add_option("-k", "--key", dest="key",
                      help="Please enter key")
    parser.add_option("-v", "--value", dest="value",
                      help="Please enter value")
    (options, args) = parser.parse_args()

    if (options.operation == None) or (options.server == None) or (options.key == None):
        parser.print_help()
        exit(0)
    else:
        operation = options.operation 
        server = options.server
        key = options.key
        value = options.value
        if operation == 'get':
            response = key_get(key, server)
            print(response)
        elif operation == 'set':
            response = key_set(key, value, server)
            print(response)
        elif operation == 'watch':
            key_watch(key, server)
        else:
            print("Please specify correct operation refer help")

