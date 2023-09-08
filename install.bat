@setlocal enableextensions
@cd /d "%~dp0"
@echo off
pip install requests pyinstaller

if %errorlevel% neq 0 (
    echo Installation failed. Please check for errors above.
    pause
    exit /b %errorlevel%
)

pyinstaller --onefile getrepos.py

if %errorlevel% neq 0 (
    echo PyInstaller failed. Please check for errors above.
    pause
    exit /b %errorlevel%
)

set "exe_directory=%cd%\dist"
echo Do you want to add the directory to the PATH? (y/n)
set /p "choice="
if /i "%choice%"=="y" (
    REM Add the directory containing getrepos.exe to the PATH
    setx PATH "%PATH%;%exe_directory%" /M
    echo Directory %exe_directory% added to the PATH.
) else (
    echo Directory %exe_directory% was not added to the PATH.
)

pause