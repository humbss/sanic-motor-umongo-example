
import aiotask_context as context
import asyncio
from sanic.log import logger
from pymongo import MongoClient
from umongo import Instance
from motor.motor_asyncio import AsyncIOMotorClient

db = None
instance = None

'''
    Connects to Mongo DB, store client+collection into var.
    this is using a test collection called test_umongo, is higly 
    recommended to change by a function argument.
'''
def connect(db_host, db_port, loop):
    logger.info("[DB] Establishing DB connection to: %s:%s ", db_host, db_port)
    global db
    db = AsyncIOMotorClient(db_host, db_port, io_loop=loop)['test_umongo']
    global instance
    instance = Instance(db)
    return instance


'''
    Retrieve mongo database connection if it exists, else create one.
    DB connection has been stored into db variable, host and port came
    from context.
'''
def get_connection():
    try:
        if instance is not None:
            return instance
        raise Exception('DB connection not found.')
    except Exception as e:
        return connect('localhost', 27017, asyncio.get_event_loop())
