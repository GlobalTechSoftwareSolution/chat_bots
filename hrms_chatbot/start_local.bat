@echo off
set LOCAL_TESTING=true
set LOCAL_DATA_DIR=./local_data
uvicorn main:app --host 0.0.0.0 --port 8000