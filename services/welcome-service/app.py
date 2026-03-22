from fastapi import FastAPI
import random

app = FastAPI()

MESSAGES = [
    "Hello from Kubernetes!",
    "Welcome from the cluster!",
    "Greetings from Helm!",
    "Hi there from your demo app!",
    "A random welcome from pod one!"
]

@app.get("/welcome")
def welcome():
    return {"message": random.choice(MESSAGES)}
