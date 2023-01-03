import pymongo
client = pymongo.MongoClient("mongodb+srv://Anugrah123:Boon1964@anugrah.aejqxhf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {"name" : "anugrah","email" : "anugrahmohan@gmail.com", "surname" : "mohan"}

db1= client['mongotest']
coll = db1['test']
coll.insert_one(d )
