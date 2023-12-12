# Deploy FastAPI on Render

## References
- [FastAPI -> Learn -> Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Create A REST API with FastAPI, SQLAlchemy and PostgreSQL.](https://youtu.be/2g1ZjA6zHRo?si=RtZQhApZhOEO9Q_H)


## Create Environment

### WSL
```
$ conda create -n fastfly python=3.10
$ conda activate fastfly
$ pip install "fastapi[all]"
$ pip install SQLAlchemy
$ pip install psycopg2-binary
$ pip install asyncpg

$ uvicorn main:app --reload
```

### Insert items
```
$ curl -X POST localhost:8000/items \
-H "Content-Type: application/json" \
-d '{"id": 1, "name": "Milk", "price": 2000, "description": "Nice milk", "on_offer": true}'

$ curl -X POST https://fastfly.onrender.com/items \
-H "Content-Type: application/json" \
-d '{"id": 1, "name": "Milk", "price": 2000, "description": "Nice milk", "on_offer": true}'
```
```
$ curl -X POST localhost:8000/items \
-H "Content-Type: application/json" \
-d '{"id": 2, "name": "Coffee", "price": 5000, "description": "Nice coffee", "on_offer": false}'
```
### List Items

### Update
```
$ curl -X PUT localhost:8000/item/1 \
-H "Content-Type: application/json" \
-d '{"id": 1, "name": "Milk", "price": 1500, "description": "Nice milk rebate", "on_offer": true}'
```

### Delete
```
$ curl -X DELETE localhost:8000/item/5 \
-H "Content-Type: application/json" \
-d '{"id": 4, "name": "Coffee", "price": 5000, "description": "Nice coffee", "on_offer": false}'
```

### Connect WSL2 to Window's Postgres database

Follow these intructions: 
https://stackoverflow.com/a/67596486







Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

See https://render.com/docs/deploy-fastapi or follow the steps below:

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!