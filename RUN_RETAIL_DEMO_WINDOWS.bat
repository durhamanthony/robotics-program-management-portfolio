@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  py -3.12 -m venv .venv
  if errorlevel 1 goto :error
)

".venv\Scripts\python.exe" -m pip install -r simulations\requirements.txt
if errorlevel 1 goto :error

echo Running the inbound-to-fulfillment retail workflow and evidence checks...
".venv\Scripts\python.exe" simulations\retail_humanoids\run_demo.py --duration 36 --output-dir outputs
if errorlevel 1 goto :error

echo Opening the order-picking MuJoCo viewer. The browser video adds the truck-unload and stocking model before this scene...
".venv\Scripts\python.exe" simulations\retail_humanoids\run_demo.py --viewer --duration 36 --output-dir outputs
if errorlevel 1 goto :error

echo.
echo Retail inbound, stair, order-pick, and courtesy-drop-off checks completed. Evidence is in the outputs folder.
pause
exit /b 0

:error
echo.
echo The retail workflow stopped because an error occurred. Keep this window open and take a screenshot.
pause
exit /b 1
