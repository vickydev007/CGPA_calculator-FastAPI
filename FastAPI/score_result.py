from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class student(BaseModel):
    name:str
    point1:int
    point2:int
    point3:int
    point4:int
    point5:int
    point6:int
    point7:int
    point8:int
    credit1:int
    credit2:int             
    credit3:int
    credit4:int
    credit5:int
    credit6:int
    credit7:int
    credit8:int

@app.get("/")
def home():
    return {"Home": "I'm your server running here"}

@app.post("/i_get_input_and_return_result")
def check(input:student):
    total=input.point1*input.credit1+input.point2*input.credit2+input.point3*input.credit3+input.point4*input.credit4+input.point5*input.credit5
    total_credit=input.credit1+input.credit2+input.credit3+input.credit4+input.credit5
    gpa=total/total_credit
    return {"Name": input.name, "GPA": gpa}