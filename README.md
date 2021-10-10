# Key-Value DB

Key_Value DB  is a cloud-enabled program for storing key value objects this attempt is to create a simple file-based key-value database written in Python.


# Server :
## Features

- Set : This operation is used to set a key a value pair in a DB.
- Get : This operation is used to get a value for a particular key.
- Remove : This operation removes a key value from DB.
- Subscribe : This is used to get updates whenever a particular key is changed.
- Unsubscribe : This is used to unsubscribe from updates for a key.

## Tech

Key value DB uses a number of open source tools to work properly:

- Python3
- Kubernetes 1.18+ (Along with storage class for persistence)
- Docker
- Helm3
- Jenkins

## Installation

Python3 based installation :

```sh
 pip3 install -r src/requirements.txt
 mkdir /data
 echo "{}" > /data/db.json
 python3 src/server/app.py
```


Docker based installation : 

```sh
docker run -p 8080:5000 -itd sagararora24/grofers-kv:1.0.1
```


Kubernetes based installation :


```sh
cd infra/charts/grofers-keyvalue/
helm install grofers-keyvalue . --namespace test --create-namespace
```
## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| autoscaling.enabled | bool | `false` |  |
| autoscaling.maxReplicas | int | `100` |  |
| autoscaling.minReplicas | int | `1` |  |
| autoscaling.targetCPUUtilizationPercentage | int | `80` |  |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"sagararora24/grofers-kv"` |  |
| image.tag | string | `"1.0.1"` |  |
| imagePullSecrets | list | `[]` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| persistence.accessMode | string | `"ReadWriteOnce"` |  |
| persistence.enabled | bool | `true` |  |
| persistence.size | string | `"8Gi"` |  |
| persistence.storageClass | string | `"efs-sc"` |  |
| podAnnotations | object | `{}` |  |
| podSecurityContext | object | `{}` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| securityContext | object | `{}` |  |
| service.port | int | `5000` |  |
| service.type | string | `"NodePort"` |  |
| tolerations | list | `[]` |  |



## Usage

### HTTP API Endpoints
1. `/get?key=<key-goes-here>` (Method: `GET`): This API endpoint is an interface to Key value DB `db_get()` method. e.g.:

```bash
curl -XGET http://localhost:5000/get?key=test
```
2. `/set` (Method: `POST`): This API endpoint is an interface to Key value DB `db_set()` method. e.g.:

```bash
curl -XPOST http://localhost:5000/set -H 'Content-Type: application/json' -d '{"key": "test", "value": "1234"}'
```
3. `/remove/<key-goes-here>` (Method: `DELETE`): This API endpoint is an interface to Key value DB `db_remove()` method. e.g.:

```bash
curl -XDELETE http://localhost:5000/remove/test
```
4. `/items` (Method: `GET`): This API endpoint is an interface to Key value DB `db_items()` method. e.g.:

```bash
curl -XGET http://localhost:5000/items
```

5. `/subscribe` (Method: `POST`): This API endpoint is an interface to Key value DB `subscribe()` method. e.g.:

```bash
curl -XPOST http://localhost:5000/subscribe -H 'Content-Type: application/json' -d '{"key": "test"}'
```
6. `/unsubscribe` (Method: `POST`): This API endpoint is an interface to Key value DB `unsubscribe()` method. e.g.:

```bash
curl -XPOST http://localhost:5000/unsubscribe -H 'Content-Type: application/json' -d '{"key": "test"}'
```

# Client

## Features

- Set : This operation is used to set a key a value pair in a DB
- Get : This operation is used to get a value for a particular key.
- Watch : Realtime view operation at interval of 5 seconds on a specific key

## Tech

Key value DB uses a number of open source tools to work properly:

- Python3

## Installation & Usage

Python3 based installation :

```sh
pip3 install -r src/requirements.txt
echo "To list CLI helper details"
python3 cli.py -h 
```

Example Set operation cli call :

```sh
python3 cli.py -o set -s http://<IP>:<Port> -k <key> -v <value>
```

## Helper for cli
```sh
Usage: cli.py [options]

Options:
  -h, --help            show this help message and exit
  -o OPERATION, --operation=OPERATION
                        Choose Operation 1. set , 2. get , 3. watch
  -s SERVER, --server=SERVER
                        Please enter server along with HTTP/HTTPS , example:
                        http://<server:port>
  -k KEY, --key=KEY     Please enter key
  -v VALUE, --value=VALUE
                        Please enter value
                        
```

