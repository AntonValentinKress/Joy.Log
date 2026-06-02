from fastapi import FastAPI, APIRouter, UploadFile, File, Form
from fastapi.responses import RedirectResponse

from datetime import time, date, datetime, timedelta
from typing import List, Annotated

from .schemas.log_entry import LogEntry

app = FastAPI()

# @app.get("/")
# async def root():
#     return RedirectResponse("/docs")

@app.post("/log")
async def post_entry(
    date: date = Form(...),
    time: time = Form(...),
    text: str = Form(...),
    score: int | None = Form(None),
    file: UploadFile | None = File(None),
    ):
    return file.filename
