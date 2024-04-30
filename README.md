# Todo FastAPI Backend


## Parameters
- `-e DB_CRED_FILE_PATH="/etc/secrets/db_cred.json"`: Path to the json file containing username and password for MySQL/MariaDB.
```json
{
  "username": "username",
  "password": "password"
}
```
- `-e DB_CONNECTION_FILE_PATH="/etc/secrets/db_conn.json"`: Path to the json file containing endpoint and DB name for MySQL/MariaDB.
```json
{
  "db_name": "db_name",
  "primary_endpoint": "primary_endpoint.com"
}
```
- `-e PORT=8000`: Listening port of the container. Default: 8000

## Run directly (required Python 3.x)
```
pip install -r requirements.txt
export DB_CRED_FILE_PATH="/etc/secrets/db_cred.json"
export DB_CONNECTION_FILE_PATH="/etc/secrets/db_conn.json"
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Docker run

```
docker run \
-d \
--name todo-backend \
-e DB_CRED_FILE_PATH="/etc/secrets/db_cred.json" \
-e DB_CONNECTION_FILE_PATH="/etc/secrets/db_conn.json" \
-e APP_PORT=8000 \
-p 8000:8000/tcp \
longhtran91/todo-backend
```
## Docker compose
```
version: '3.1'

services:
  todo-backend:
    container_name: todo-backend
    environment:
      - DB_CRED_FILE_PATH="/etc/secrets/db_cred.json"
      - DB_CONNECTION_FILE_PATH="/etc/secrets/db_conn.json"
      - APP_PORT=8000
    ports:
      - 8000:8000/tcp
    image: longhtran91/todo-backend
```
## Kubernetes (EKS, Secrets Store CSI with AWS)
```
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: todo
  namespace: todo
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::{account}:role/{role_name}
---
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: rds-db-secret
  namespace: todo
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "{param_name}"
        objectType: ssmparameter
        objectAlias: "db_conn.json"
      - objectName: "{secret_name}"
        objectType: secretsmanager
        objectAlias: db_cred.json
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: todo-backend-deployment
  namespace: todo
  labels:
    app: todo-backend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: todo-backend
  template:
    metadata:
      labels:
        app: todo-backend
    spec:
      serviceAccountName: todo
      containers:
        - name: todo-backend
          image: longhtran91/todo-backend
          imagePullPolicy: Always
          ports:
            - containerPort: 8000
          env:
            - name: APP_PORT
              value: "8000"
            - name: DB_CRED_FILE_PATH
              value: /etc/secrets/db_cred.json
            - name: DB_CONNECTION_FILE_PATH
              value: /etc/secrets/db_conn.json
          volumeMounts:
            - name: db-secret
              mountPath: /etc/secrets
              readOnly: true
      volumes:
        - name: db-secret
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: rds-db-secret
```
## API Docs

### `/metrics`

#### `GET`
##### Summary:
Metrics

##### Description:
Endpoint that serves Prometheus metrics.

##### Responses
| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |


### API: `/todos/`
#### Method: `POST`
##### Summary:
Create Todo

##### Responses
> | Code | Description |
> | ---- | ----------- |
> | 201 | Successful Response |
> | 422 | Validation Error |

#### Method: `GET`
##### Summary:

Read Todos

##### Parameters

> | Name | Located in | Description | Required | Schema |
> | ---- | ---------- | ----------- | -------- | ---- |
> | skip | query |  | No | integer |
> | limit | query |  | No | integer |

##### Responses

> | Code | Description |
> | ---- | ----------- |
> | 200 | Successful Response |
> | 422 | Validation Error |

### API: `/todos/{todo_id}`

#### Method: `GET`
##### Summary:

Read Todo

##### Parameters

> | Name | Located in | Description | Required | Schema |
> | ---- | ---------- | ----------- | -------- | ---- |
> | todo_id | path |  | Yes | integer |

##### Responses

> | Code | Description |
> | ---- | ----------- |
> | 200 | Successful Response |
> | 422 | Validation Error |

#### Method: `PUT`
##### Summary:

Update Todo

##### Parameters

> | Name | Located in | Description | Required | Schema |
> | ---- | ---------- | ----------- | -------- | ---- |
> | todo_id | path |  | Yes | integer |

##### Responses

> | Code | Description |
> | ---- | ----------- |
> | 200 | Successful Response |
> | 422 | Validation Error |

#### Method: `DELETE`
##### Summary:

Delete Todo

##### Parameters

> | Name | Located in | Description | Required | Schema |
> | ---- | ---------- | ----------- | -------- | ---- |
> | todo_id | path |  | Yes | integer |

##### Responses

> | Code | Description |
> | ---- | ----------- |
> | 204 | Successful Response |
> | 422 | Validation Error |

### API: `/health`

#### Method: `GET`
##### Summary:

Check Health

##### Responses

> | Code | Description |
> | ---- | ----------- |
> | 200 | Successful Response |
