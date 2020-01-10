import json
from util.umongo_connection import get_connection
from bson.objectid import ObjectId
from sanic.response import text
from pymongo.errors import ServerSelectionTimeoutError
from sanic.log import logger
from sanic.exceptions import ServerError
from model.user import User

async def register_user(user_param):
    try:
        new_user = User(**json.loads(user_param.body))
        await new_user.commit()
        return new_user.dump()
    except ServerSelectionTimeoutError as e:
        logger.error("[DB] Error connecting to database: %s",e)
        raise ServerError("Service Error", status_code=500)

async def get_user(id):
    try:
        result = await User.find_one({"_id": ObjectId(id)})
        return result.dump()
    except ServerSelectionTimeoutError as e:
        logger.error("[DB] Error connecting to database: %s",e)
        raise ServerError("Service Error", status_code=500)

