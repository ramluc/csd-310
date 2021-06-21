from pymongo import MongoClient;
#Create a variable named url and assign it the connection string value you copied from MongoDB Atlas.
url = "mongodb+srv://admin:admin@cluster0.ivifd.mongodb.net/pytech";
#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url);
#Create a variable named db and assign it to the pytech database instance.
db = client.pytech;
print("-- Pytech C0llection List --");
#Using Python’s built-in print statement, calling the list_collection_names method off of the db variable.
print(db.list_collection_names());
print("");
#could not find a good way to exit while only hitting 1 key so just faked it
print('Press a key to exit')

