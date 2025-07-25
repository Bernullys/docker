from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "Hello How are you"

@app.get("/how are you")
def hello():
    return "I'm good, how about you"