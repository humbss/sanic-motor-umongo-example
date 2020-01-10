from umongo import Instance, Document, fields
from pymongo import MongoClient
from umongo import Instance
from util.umongo_connection import get_connection

instance = get_connection()

@instance.register
class User(Document):
    name = fields.StringField(required=True, unique=False)
    email = fields.EmailField(required=True, unique=False)
