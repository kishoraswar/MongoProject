import pymongo
client = pymongo.MongoClient("mongodb+srv://mongo:Welcome2022@cluster0.itrfmco.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "kishor",
    "email" : "kishoraswar22@gmail.com",
    "surname" : "aswar"

}



db1 = client['mongotest']
coll = db1['test1']
coll.insert_one(d)