import os
import requests
from pydantic import BaseModel
from fastapi.responses import JSONResponse


def request(payload: BaseModel, endpoint: str) -> JSONResponse:
    server = os.environ["SERVER"]
    url = f"{server}/{endpoint}"
    res = requests.post(url, json=payload.__dict__)
    return JSONResponse(status_code=res.status_code, content=res.json())
