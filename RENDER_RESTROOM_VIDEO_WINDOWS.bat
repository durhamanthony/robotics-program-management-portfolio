@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Python environment not found. Run RUN_RESTROOM_DEMO_WINDOWS.bat setup instructions first.
  pause
  exit /b 1
)

echo Rendering the approved 146-second restroom demonstration...
".venv\Scripts\python.exe" scripts\render_mujoco_videos.py restroom --width 960 --height 540 --fps 15
if errorlevel 1 goto :error

echo Rebuilding the website so the new MP4 is copied into docs...
".venv\Scripts\python.exe" scripts\build_portfolio_site.py
if errorlevel 1 goto :error

echo.
echo Restroom video and website files are ready for GitHub Desktop review.
pause
exit /b 0

:error
echo.
echo Rendering or website rebuild failed. Keep this window open and share the error.
pause
exit /b 1
