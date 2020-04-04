# TruckPad Challenge API

> This a Flask application using MongoDB as DBMS running in Docker

### Usefull links
- Swagger Documentation: `/api/docs`
- [Docker Docs](https://docs.docker.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [MongoDB](https://www.mongodb.com/) and [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
- [pytest](https://docs.pytest.org/en/latest/index.html)
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/#)


### How to install

First of all, you need to install [Docker](https://docs.docker.com/install/)

After, clone this repo:
```bash
git clone https://github.com/allanzi/truck-challenge.git
```

Run containers of api:
```bash
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

Running tests
```bash
docker exec -it back_challenge_app py.test -s
```

### Routes
| Method  |  Description  | Route  | Body |
| :------------ | :---------------| :---------------| :-----|
| GET           | Get all users   | `/api/users`   |    |
| GET           | Show an user    | `/api/users/{userId}`   |    |
| PUT           | Update an user  | `/api/users/{userId}`   |  ` { "age": 18 }`  |
| DELETE        | Delete an user  | `/api/users/{userId}`   |   |
| POST          |  Create user    | `/api/users`   | ` { "name": "Allan Santos", "age": 20, "driver_license_type": "B", "is_busy": false, "has_vehicle": true, "vehicle_type_id": 1 }` |
| GET           | Get all users bused | `/api/reports/bused-users`   |    |
| GET           | Get all users has vehicle  |`/api/reports/users-has-vehicle`   |    |
| GET           | Get report Daily, Weekly and Monthly of the quantity trucks use the terminal  | `/api/reports/terminals`   |    |
| POST          | Create terminal usage  | `/api/terminals`   |  `{ "user_id": "5e86b444c9c0aa7704892dc2", "is_busy": false }`  |
| GET           | Show all travels  | `/api/travels`   |    |
| POST          | Create an travel  | `/api/travels`   |   ` { "from_": { "latitude": -16.32972, "longitude": -154.96172 }, "to": { "latitude": 4.18978, "longitude": -112.71793 }, "user_id": "5e86b444c9c0aa7704892dc2" }` |
| GET           | Show an travel  | `/api/travels/{travelId}`   |    |
| UPDATE        | Update an travel  | `/api/travels/{travelId}`   |  ` { "to": { "latitude": 4.18978, "longitude": -112.71793 } }`  |
| DELETE        | Delete an travel  | `/api/travels/{travelId}`   |    |
| GET           | Show all travels group by user  | `/api/reports/travels`   |    |