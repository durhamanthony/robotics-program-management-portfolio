@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  py -3.12 -m venv .venv
  if errorlevel 1 goto :error
)

".venv\Scripts\python.exe" -m pip install -r simulations\requirements.txt
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\render_mujoco_videos.py retail --width 960 --height 540 --fps 15
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\build_portfolio_site.py
if errorlevel 1 goto :error

".venv\Scripts\python.exe" scripts\validate_portfolio.py
if errorlevel 1 goto :error

echo.
echo Retail video rendered, website rebuilt, and validation passed.
pause
exit /b 0

:error
echo.
echo Retail rendering or validation failed. Keep this window open and take a screenshot.
pause
exit /b 1
