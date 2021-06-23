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
liam = {
"student_id": "1010",
"first_name": "Liam",
"last_name": "Johnson",
"enrollments": [
    {
    "term": "Cohort 2",
    "gpa": "May 25, 2021",
    "end_date": "July 24th, 2021",
    "courses": [
        {
        "course_id": "CSD",
        "description": "Database Development",
        "instructor": "Professor Sampson",
        "grade": "A"
        }
    ]
    }
]
}
#adds data to table and prints the document id
liam_student=col.insert_one(liam).inserted_id;
print("")
print("")
print("-- INSERT STATEMENTS --")
print("Inserted student record Fred Johnson into the student collection with document id: "+ str(liam_student));
 #pulls updates specific student then prints the new data
print("-- DISPLAYING STUDENT Test DOC --");
doc = col.find_one({"student_id": "1010"});
print("Student ID: "+str(doc["student_id"]));
print("First Name: "+str(doc["first_name"]));
print("Last Name: "+str(doc["last_name"]));
col.delete_one({"student_id":"1010"});
print("")
print("")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --");
 #loops through all data and parses it to look nice
for doc in col.find():
 print("Student ID: "+str(doc["student_id"]));
 print("First Name: "+str(doc["first_name"]));
 print("Last Name: "+str(doc["last_name"]));
 print("")
#fake it till you make it
print("")
print("")
print("End of program, press any key to exit...")
