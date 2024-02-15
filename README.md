#TEST DEV#1
#TEST DEV#2
#TEST DEV#3
#TEST DEV#4
#TEST DEV#5
# Todo FastAPI Backend


## Parameters
- `-e DB_STRING_FILE_PATH="/etc/secrets/db_string"`: Path to the file containing DB string for MySQL/MariaDB. [More information on the content of the file](https://docs.sqlalchemy.org/en/20/dialects/mysql.html)
- `-e PORT=8000`: Listening port of the container. Default: 8000

## Run directly (required Python 3.x)
```
pip install -r requirements.txt
export DB_STRING_FILE_PATH="/etc/secrets/db_string"
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Docker run

```
docker run \
-d \
--name todo-backend \
-e B_STRING_FILE_PATH="/etc/secrets/db_string" \
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
      - DB_STRING_FILE_PATH="/etc/secrets/db_string"
      - APP_PORT=8000
    ports:
      - 8000:8000/tcp
    image: longhtran91/todo-backend
```
## Kubernetes
```
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
      containers:
        - name: todo-backend
          image: longhtran91/todo-backend
          imagePullPolicy: Always
          ports:
            - containerPort: 8000
          env:
            - name: APP_PORT
              value: "8000"
            - name: DB_STRING_FILE_PATH
              value: /etc/secrets/db_string
          volumeMounts:
            - name: db-string-vol
              mountPath: /etc/secrets
      volumes:
        - name: db-string-vol
          secret:
            secretName: db-secret
---
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
  namespace: todo
type: Opaque
data:
  db_string: bXlzcWwrcHlteXNxbDovL3Jvb3Q6cGFzc3dvcmRAbWFyaWFkYi1zdmMvdG9kby1kZXYtZGI=
```
## API Docs
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
