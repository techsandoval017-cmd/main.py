from fastapi import FastAPI, Request, Header, HTTPException
import os
import sqlite3
import stripe

app = FastAPI(title="S-PRIME VÓRTEX Core")

@app.get("/")
def read_root():
    return {"status": "S-PRIME CORE ONLINE", "rango": "S"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
