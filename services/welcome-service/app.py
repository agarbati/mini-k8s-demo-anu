from fastapi import FastAPI
import random

app = FastAPI()

MESSAGES = [
    "Hello123 from Kubernetes!",
    "WelcomeXYZ from the cluster!",
    "Greetings890 from Helm!",
    "Hi there from your demo app!",
    "Hi there I am a moron!",
    "Hi there I am a moron1!",
    "Hi there I am a moron2!",
    "Hi there I am a moron3!",
    "Hi there I am a moron4!",
    "Hi there I am a moron5!",
    "Hi there I am a moron6!",
    "A9999 random welcome from pod one!"
]

@app.get("/welcome")
def welcome():
    return {"message": random.choice(MESSAGES)}
