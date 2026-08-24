@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  py -3.12 -m venv .venv
  if errorlevel 1 goto :error
)

".venv\Scripts\python.exe" -m pip install -r simulations\requirements.txt
if errorlevel 1 goto :error

".venv\Scripts\python.exe" tools\support-operations-lab\build_cases.py --output-dir outputs\support_workflow
if errorlevel 1 goto :error

".venv\Scripts\python.exe" simulations\retail_humanoids\run_demo.py --duration 36 --output-dir outputs
if errorlevel 1 goto :error

".venv\Scripts\python.exe" simulations\open_quadruped_raas\run_demo.py --duration 36 --output-dir outputs
if errorlevel 1 goto :error

".venv\Scripts\python.exe" simulations\test_models.py
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\build_demo_videos.py support
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\build_portfolio_site.py
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\validate_portfolio.py
if errorlevel 1 goto :error

echo.
echo Portfolio workflow, models, website, links, evidence labels, and required artifacts passed.
pause
exit /b 0

:error
echo.
echo Validation stopped because a check failed. Keep this window open and take a screenshot.
pause
exit /b 1
