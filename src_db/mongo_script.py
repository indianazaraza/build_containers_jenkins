from pymongo import MongoClient

conn = MongoClient("mongodb://localhost")
db = conn["library"]
collection = db["books"]

book1 = {"name":"Ulises", "author":"James Joy"}

book2 = {"name":"El Gatopardo", "author":"Giuseppe Tomasi di Lampedusa"}

book3 = {"name":"Sangre fría", "author":"Truman Capote"}

collection.insert_many([book1, book2, book3])

results = collection.find()

for result in results:
	print(result["name"])
