from pymongo import MongoClient
from dotenv import load_dotenv
import os

uri = os.getenv("MONGO_URI")

conn = MongoClient(uri)
