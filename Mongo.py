from pymongo import MongoClient
from collections import OrderedDict
import sys

client = MongoClient('mongodb://localhost:27017/')
db = client.dbbname
db.create_collection("coll")

schema={"$jsonSchema":
          {
              "bsonType": "object",
              "required": ["name", "year", "major", "gpa"],
              "properties": {
                  "name": {
                      "bsonType": "string",
                      "description": "must be a string and is required"
                  },
                  "gender": {
                      "bsonType": "string",
                      "description": "must be a string and is not required"
                  },
                  "year": {
                      "bsonType": "int",
                      "minimum": 2017,
                      "maximum": 3017,
                      "exclusiveMaximum": False,
                      "description": "must be an integer in [ 2017, 3017 ] and is required"
                  },
                  "major": {
                      "enum": ["Math", "English", "Computer Science", "History", None],
                      "description": "can only be one of the enum values and is required"
                  },
                  "gpa": {
                      "bsonType": ["double"],
                      "minimum": 0,
                      "description": "must be a double and is required"
                  }
              }
          }
          }

cmd = OrderedDict([('collMod', 'coll'), ('validator', schema),('validationAction', 'warn')])
db.command(cmd)
db.coll.insert_one({'fsdfsfsd': 'fasfasdads'})
