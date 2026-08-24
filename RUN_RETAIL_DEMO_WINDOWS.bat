@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  py -3.12 -m venv .venv
  if errorlevel 1 goto :error
)

".venv\Scripts\python.exe" -m pip install -r simulations\requirements.txt
if errorlevel 1 goto :error

echo Running the fast retail workflow and evidence check...
".venv\Scripts\python.exe" simulations\retail_humanoids\run_demo.py --duration 36 --output-dir outputs
if errorlevel 1 goto :error

echo Opening the retail MuJoCo viewer with the corrected overview camera and stair heights...
".venv\Scripts\python.exe" simulations\retail_humanoids\run_demo.py --viewer --duration 36 --output-dir outputs
if errorlevel 1 goto :error

echo.
echo Retail workflow completed. Evidence is in the outputs folder.
pause
exit /b 0

:error
echo.
echo The retail workflow stopped because an error occurred. Keep this window open and take a screenshot.
pause
exit /b 1
