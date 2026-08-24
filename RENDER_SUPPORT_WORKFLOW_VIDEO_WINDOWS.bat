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

".venv\Scripts\python.exe" scripts\build_demo_videos.py support
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\build_portfolio_site.py
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\validate_portfolio.py
if errorlevel 1 goto :error

echo.
echo Support data workflow, animation, website, and validation completed.
pause
exit /b 0

:error
echo.
echo Support workflow rendering or validation failed. Keep this window open and take a screenshot.
pause
exit /b 1
