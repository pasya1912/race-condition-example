from fastapi import FastAPI
import time
import threading

app = FastAPI()
used = 0  # Shared resource
balance = 0
lock = threading.Lock()

@app.post("/increment")
def increment():
    # Read-modify-write is NOT atomic
    global balance
    global used
    global lock
    with lock:
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