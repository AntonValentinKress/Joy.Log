@echo off

call .\.venv\Scripts\activate
call uvicorn src.main:app --host 0.0.0.0 --port 10000 --reload