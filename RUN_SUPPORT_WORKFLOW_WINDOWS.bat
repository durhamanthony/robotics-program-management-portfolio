@echo off
setlocal
cd /d "%~dp0"

py -3.12 tools\support-operations-lab\build_cases.py
if errorlevel 1 goto :error

echo.
echo Data-only support workflow passed. Results are in outputs\support_workflow.
pause
exit /b 0

:error
echo.
echo The support workflow failed. Keep this window open and take a screenshot.
pause
exit /b 1
