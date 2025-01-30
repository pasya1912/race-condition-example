from fastapi import FastAPI
import time
import threading
from pydantic import BaseModel

app = FastAPI()

# Shared resource
balances = {"user1": 100, "user2": 0}
withdraw_data = {"user1": 0, "user2": 0}

# Locks for thread safety
withdraw_lock = threading.Lock()
transfer_lock = threading.Lock()

class Transfer(BaseModel):
    amount: int
    userid: str

class WithdrawClass(BaseModel):
    amount: int

@app.post("/withdraw")
def withdraw(data: WithdrawClass):
    global balances
    global withdraw_data
    global withdraw_lock
    amount = data.amount
    with withdraw_lock:
        current = balances["user1"]
        time.sleep(75 / 1000)  # Simulate some processing time
        if current >= amount:
            balances["user1"] = current - amount
            withdraw_data["user1"] += amount
    return balances

@app.post("/transfer")
def transfer(data: Transfer):
    global balances
    global transfer_lock
    userid = data.userid
    amount = data.amount
    with transfer_lock:
        current = balances["user1"]
        time.sleep(75 / 1000)  # Simulate some processing time
        balances["user1"] = current - amount
        balances[userid] = balances.get(userid, 0) + amount
    return balances

@app.get("/status")
def get_balance(userid: str):
    global balances
    global withdraw_data
    return {"balance": balances[userid],"withdraw":withdraw_data[userid]}