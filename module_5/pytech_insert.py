from pymongo import MongoClient;
#Create a variable named url and assign it the connection string value you copied from MongoDB Atlas.
url = "mongodb+srv://admin:admin@cluster0.ivifd.mongodb.net/pytech";
#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url);
#Create a variable named db and assign it to the pytech database instance.
db = client.pytech;
#pulls table from pytech database
col=db.students;
#creates fred's data
print("-- INSERT STATEMENTS --")
fred = {
"student_id": "1007",
"first_name": "Fred",
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
fred_student_id = col.insert_one(fred).inserted_id;
print("Inserted student record Fred Johnson into the student collection with document id: "+ str(fred_student_id));
#creates john's data
john = {
"student_id": "1008",
"first_name": "John",
"last_name": "Smith",
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
john_student_id = col.insert_one(john).inserted_id;
print("Inserted student record John Smith into the student collection with document id: "+ str(john_student_id));
#creates mike's data
mike = {
"student_id": "1009",
"first_name": "Mike",
"last_name": "Wildos",
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
mike_student_id = col.insert_one(mike).inserted_id;
print("Inserted student record Mike Wildos into the student collection with document id: " + str(mike_student_id));
print("")
print("End of program, press any key to exit...")
