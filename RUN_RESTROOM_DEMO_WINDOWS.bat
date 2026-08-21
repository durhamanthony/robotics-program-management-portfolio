@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo.
  echo Python environment not found in this repository.
  echo First run: py -3.12 -m venv .venv
  echo Then run: .venv\Scripts\python.exe -m pip install -r simulations\requirements.txt
  echo.
  pause
  exit /b 1
)

echo Opening the public-restroom MuJoCo v4 two-loop audit...
".venv\Scripts\python.exe" simulations\restroom_cleaning\run_demo.py --viewer

if errorlevel 1 (
  echo.
  echo The demo ended with an error. Keep this window open and share the message.
  pause
)
