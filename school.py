import pymongo
import pprint


connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
student = db.students


def find():
    query = {"scores.type": "homework"}
    score = {'scores': 'score'}

    print('Search result ')
    cursor = student.find(query).limit(20)
    # print(cursor)
    for doc in cursor:
        print(doc)

find()
