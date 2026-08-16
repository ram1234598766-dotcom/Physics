@echo off
rem ============================================================
rem  Structure-Flow Calculus - one-click local docs
rem  Installs the dependencies on first run, starts the site,
rem  and opens your browser. Requires Node.js.
rem ============================================================
setlocal
cd /d "%~dp0"

where node >nul 2>nul
if errorlevel 1 (
  echo Node.js was not found on this machine.
  echo Install it from https://nodejs.org and then run this file again.
  pause
  exit /b 1
)

if not exist node_modules (
  echo First run: installing dependencies with npm...
  call npm install
  if errorlevel 1 (
    echo.
    echo Installation failed. Check the error above, then run this file again.
    pause
    exit /b 1
  )
  echo Done.
) else (
  echo Dependencies already installed.
)

echo.
echo Starting the documentation site - your browser will open shortly.
echo Press Ctrl+C in this window to stop the server.
echo.
start "" /b cmd /c "timeout /t 5 /nobreak >nul & start http://localhost:5173"
npm run docs:dev

pause
