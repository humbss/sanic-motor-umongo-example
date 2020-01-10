# sanic-motor-example
Python 3+ event-loop application using Sanic as framework fully integrated with Motor and uMongo as async/await ODM.


![sanic](https://raw.githubusercontent.com/huge-success/sanic-assets/master/png/sanic-framework-logo-white-400x97.png)

![motor](https://motor.readthedocs.io/en/stable/_images/motor.png)


## Setup Project

1. Create virtual environment (in clone directory):

    `python3 -m venv ./envi`

    Activate the new environment

    `source ./envi/bin/activate`

2. Install dependencies

    `pip3 install -r requirements.txt `

3. Create .env file with the following content:

    `SANIC_dbhost=localhost`

    `SANIC_dbport=27017`

4. Bring mongp up with docker-compose file:

    `docker-compose up`

5. Run app

    `make runserver-dev`


```bash
├── api
│   ├── __init__.py
│   ├── routes.py       ---> (Routes handler, configure available rest routes) 
│   └── user_API.py     ---> (User rest service API example)
├── docker-compose.yml  ---> (Mongo service)
├── main.py             ---> (Application entry point)
├── Makefile            ---> (Make scripts)
├── model
│   ├── __init__.py
│   └── user.py         ---> (DB Entity model class)
├── README.md           ---> (This file) 
├── requirements.txt    ---> (Required libs)
├── service
│   ├── __init__.py
│   └── user_service.py ---> (User api service layer, it deals with DB)
├── tests
│   └── test_user.py    ---> (Unit tests)
└── util
    ├── generic_except.py    ---> (Util for exception handling)
    ├── __init__.py
    └── umongo_connection.py ---> (Util for DB connection handling)
```

## Test Requests

`[POST]` localhost:8000/user/

Payload:
    
    {
        "email":"bill@microsoft.com",
        "name":"Sir William Gates"
    }
    
    

`[GET]` localhost:8000/user/INSERTED-ID

## Unit Tests

The directory `tests` has the unit tests (PyTest) files, you can invoke the test execution with the command:

`pytest`
 
## DOC

Swagger URL: `http://localhost:8000/swagger/`
