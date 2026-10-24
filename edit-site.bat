@echo off
rem Double-click to open the local protocol editor (tools\editor.py). Close this window to stop it.
cd /d "%~dp0"
set "PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not exist "%PY%" set "PY=python"
"%PY%" tools\editor.py %*
pause
