@echo off
title AJCZ Web Agency Installer
cls

echo AJCZ Web Agency Installer v1.0
echo.

if exist "dist\AJCZ-Web-Agency.exe" (
    echo Found: dist\AJCZ-Web-Agency.exe
    set "SOURCE_EXE=dist\AJCZ-Web-Agency.exe"
) else if exist "AJCZ-Web-Agency.exe" (
    echo Found: AJCZ-Web-Agency.exe
    set "SOURCE_EXE=AJCZ-Web-Agency.exe"
) else (
    echo ERROR: AJCZ-Web-Agency.exe not found
    echo Please ensure the file is in the current directory or dist folder
    pause
    exit /b 1
)

echo.
echo Installing to: %PROGRAMFILES%\AJCZ Web Agency
set /p "CONFIRM=Continue? (Y/N): "
if /I not "%CONFIRM%"=="Y" exit /b

echo.
echo Creating directories...
mkdir "%PROGRAMFILES%\AJCZ Web Agency" 2>nul
mkdir "%PROGRAMFILES%\AJCZ Web Agency\assets" 2>nul

echo Copying files...
copy /Y "%SOURCE_EXE%" "%PROGRAMFILES%\AJCZ Web Agency\AJCZ-Web-Agency.exe" >nul

if exist "assets\icon.ico" (
    copy /Y "assets\icon.ico" "%PROGRAMFILES%\AJCZ Web Agency\assets\icon.ico" >nul
)

echo Creating shortcuts...
set "DESKTOP=%USERPROFILE%\Desktop"
echo [InternetShortcut] > "%DESKTOP%\AJCZ Web Agency.url"
echo URL=file:///%PROGRAMFILES%\AJCZ Web Agency\AJCZ-Web-Agency.exe >> "%DESKTOP%\AJCZ Web Agency.url"

echo.
echo Installation completed!
echo Location: %PROGRAMFILES%\AJCZ Web Agency
echo.
pause
