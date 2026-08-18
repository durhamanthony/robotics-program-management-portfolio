@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  py -3.12 -m venv .venv
)

.venv\Scripts\python.exe -m pip install -r simulations\requirements.txt
if errorlevel 1 goto :error

.venv\Scripts\python.exe scripts\render_mujoco_videos.py
if errorlevel 1 goto :error

echo.
echo Six MuJoCo videos were created in media\videos.
echo Open GitHub Desktop, commit the changed MP4 files, and Push origin.
pause
exit /b 0

:error
echo.
echo Rendering stopped because an error occurred. Take a screenshot of this window.
pause
exit /b 1
