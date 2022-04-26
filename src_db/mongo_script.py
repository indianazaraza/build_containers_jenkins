from pymongo import MongoClient

with MongoClient("mongodb://172.18.0.2:27017/") as conn:
	db = conn["library"]
	collection = db["books"]

	book1 = {"name":"Ulises", "author":"James Joy"}

	book2 = {"name":"El Gatopardo", "author":"Giuseppe Tomasi di Lampedusa"}

	book3 = {"name":"Sangre fría", "author":"Truman Capote"}

	collection.insert_many([book1, book2, book3])

	results = collection.find()

	for result in results:
		print(result["name"])
