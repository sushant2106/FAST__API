from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

students={
    1:{
        "name":"Sachin",
        "Age":17,
        "year":"2023"
    }
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[str]=None
    year:Optional[str]=None

@app.get("/")
def index():
    return {"name":"First Data"}


# @app.get("/get-student/{student_id}")
# def get_student(student_id:int Path(None,description="The id of student",gt=0,lt=3)):
#     return students[student_id]


@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[student_id]

#Query Parameter --> google.com?search=name
@app.get("/get-by-name")
def get_student(*,name:Optional[str]=None,test :int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    
    return {"Data":"Not found"}



#Mixing Query and Paramter

@app.get("/get-by-both/{student_id}")
def get_student_both(*,student_id:int,name:Optional[str]=None,test :int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    
    return {"Data":"Not found"}


#Request Body and The Post Method

@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Student):
    if student_id in students:
        return {"Error":"Students exists"}
    
    students[student_id]=student
    return students[student_id]
    

#put method(it will update which is already exist)


@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    if student.name !=None:
        students[student_id].name=student.name
    
    if student.age!=None:
        students[student_id].age=student.age

    if student.year!=None:
        students[student_id].year=student.year
    
    
    return students[student_id]


    
#Delete Method

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    del students[student_id]
    return {"Message":"Student delete Sucessfully"}
