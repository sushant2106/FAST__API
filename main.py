from fastapi import FastAPI,Path
from typing import Optional


app=FastAPI()

student={
    1:{
        "name":"Sachin",
        "Age":17,
        "class":"year 22"
    }
}


@app.get("/")
def index():
    return {"name":"First Data"}


# @app.get("/get-student/{student_id}")
# def get_student(student_id:int Path(None,description="The id of student",gt=0,lt=3)):
#     return student[student_id]


@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return student[student_id]

#Query Parameter --> google.com?search=name
@app.get("/get-by-name")
def get_student(*,name:Optional[str]=None,test :int):
    for student_id in student:
        if student[student_id]["name"]==name:
            return student[student_id]
    
    return {"Data":"Not found"}



