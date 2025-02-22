from typing import Union

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root(req: Request):
  return {
    "RemoteIp": req.client.host
  }
