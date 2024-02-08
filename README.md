# Todo FastAPI Backend


## Parameters
- `DB_STRING="mysql+pymysql://user:pass@mariadb_hostname/dbname"` Database string to connect to MariaDB Support database

## Run directly (required Python 3.x)
```
pip install -r requirements.txt
export DB_STRING="mysql+pymysql://user:pass@mariadb_hostname/dbname"
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Docker run

```
docker run \
-d \
--name todo-backend \
-e DB_STRING="mysql+pymysql://user:pass@mariadb_hostname/dbname" \
-p 8000:8000/tcp \
longhtran91/todo-backend
```
## Docker compose
```
name: Todo App
services:
  todo-backend:
    container_name: todo-backend
    environment:
      - DB_STRING=mysql+pymysql://user:pass@mariadb_hostname/dbname
    ports:
      - 8000:8000/tcp
    image: longhtran91/todo-backend
```
## Kubernetes
```
---
apiVersion: v1
kind: Pod
metadata:
  name: todo-backend
spec:
  containers:
    - name: todo-backend
      image: longhtran91/todo-backend
      ports:
        - containerPort: 8000
      env:
        - name: DB_STRING
          valueFrom:
            secretKeyRef:
              name: todo-backend-secret
              key: DB_STRING
---
apiVersion: v1
kind: Secret
metadata:
  name: todo-backend-secret
type: Opaque
data:
  DB_STRING: bXlzcWwrcHltcXlvdTp1c2VyOnBhc3NAcmVmcmVzaEBtYXJpYWRiX2hvc3RvbmdpbmVkL2Ri #base64-encoded
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

### API: `/health/`

#### Method: `GET`
##### Summary:

Check Health

##### Responses

> | Code | Description |
> | ---- | ----------- |
> | 200 | Successful Response |
