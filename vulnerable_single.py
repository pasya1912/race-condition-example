from fastapi import FastAPI
import time

app = FastAPI()
used = 0  # Shared resource
balance = 0

@app.post("/increment")
def increment():
    global balance
    global used
    isUsed = used
    time.sleep(75/1000)
    if isUsed == 1:
        return {"":"limit"}

    balance += 1
    used = 1
    return {"isSuccesd": True}

@app.get("/balance")
def countered():
    global balance
    global used
    return {"balance":balance}