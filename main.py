from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    text:str

app=FastAPI()

@app.post("/")
def predict(data:Input):
    result=data.text[::-1]
    return {"input":data.text,"reverse":result}


