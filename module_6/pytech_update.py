from pymongo import MongoClient;
#Create a variable named url and assign it the connection string value you copied from MongoDB Atlas.
url = "mongodb+srv://admin:admin@cluster0.ivifd.mongodb.net/pytech";
#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url);
#Create a variable named db and assign it to the pytech database instance.
db = client.pytech;
#grabs table from the database
col=db.students;
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --");
 #loops through all data and parses it to look nice
for doc in col.find():
 print("Student ID: "+str(doc["student_id"]));
 print("First Name: "+str(doc["first_name"]));
 print("Last Name: "+str(doc["last_name"]));
 print("")

 #pulls updates specific student then prints the new data
print("-- DISPLAYING STUDENTS DOCUMENT 1007 --");
col.update_one({"student_id": "1007"}, {"$set": {"last_name": "Johnson"}})
doc = col.find_one({"student_id": "1007"});
print("Student ID: "+str(doc["student_id"]));
print("First Name: "+str(doc["first_name"]));
print("Last Name: "+str(doc["last_name"]));
#fake it till you make it
print("")
print("")
print("End of program, press any key to exit...")
