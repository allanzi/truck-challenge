# TruckPad Challenge API

> This a Flask application using MongoDB as DBMS running in Docker

### Usefull links
- Swagger Documentation: `/api/docs`
- [Docker Docs](https://docs.docker.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [MongoDB](https://www.mongodb.com/) and [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)


### How to install

First of all, you need to install [Docker](https://docs.docker.com/install/)

After, clone this repo:
```
git clone https://github.com/allanzi/truck-challenge.git
```

Run containers of api:
```
docker-compose up -d
```
> Note: in first time, Docker will build automatically

Access api python container:
```bash
docker exec -it back_challenge_app sh
```

Access api database container:
```bash
docker exec -it back_challenge_db sh
```
