@echo off

echo Starting BoughtyBOT Backend API...
uvicorn api:app --reload --host 0.0.0.0 --port 8000
pause
