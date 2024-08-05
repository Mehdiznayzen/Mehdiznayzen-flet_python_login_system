from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

@app.get("/")
def getFn() :
    return {
        "dream" : "Mehdi will be a software engineer inchallah ."
    }
    
@app.get("/calculate")
def calculate(number1: float, number2: float, operator: str) :
    if operator == "+" :
        return {
            "result" : number1 + number2
        }
    elif operator == "-" :
        return {
            "result" : number1 - number2
        }
    elif operator == "*" :
        return {
            "result" : number1 * number2
        }
    elif operator == "/" :
        if number2 != 0 :
            return {
            "result" : number1 / number2
        }
        else :
            return { 
                "message" : "You have to enter a positive number !!" 
            }
        
    if number1 and number1 :
        return {
            "message": "Enter the values !!"
        }