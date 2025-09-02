from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Input(BaseModel):
    text:str

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    
)

@app.post("/")
def predict(data:Input):
    print("Processing")
    result=data.text[::-1]
    print("processed")
    return {"input":data.text,"reverse":result}


