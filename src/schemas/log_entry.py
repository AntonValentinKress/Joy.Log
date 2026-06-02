from pydantic import BaseModel, Field
from datetime import datetime, date, time, timedelta
from fastapi import UploadFile, File

class LogEntry(BaseModel):
    date: date
    time: time
    text: str
    score: int = Field(None, ge=0, le=10)
    file: UploadFile = File(None)