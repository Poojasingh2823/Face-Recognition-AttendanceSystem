import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':""
})

ref = db.reference('Students')

data = {
    "2124":
        {
            "name": "Pooja Singh",
            "department": "CSE",
            "starting_year": 2021,
            "total_attendance": 1,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "2435":
        {
            "name": "Katrina",
            "department": "Civil",
            "starting_year": 2020,
            "total_attendance": 3,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "2564":
        {
            "name": "Emily",
            "department": "EE",
            "starting_year": 2021,
            "total_attendance": 4,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "2985":
        {
            "name": "Elon",
            "department": "CSE",
            "starting_year": 2022,
            "total_attendance": 2,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
    
}

for key, value in data.items():
    ref.child(key).set(value)