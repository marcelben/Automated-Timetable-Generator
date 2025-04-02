@echo off
echo Setting up environment...
set PYTHONPATH=%CD%
python -m pip install --upgrade pip
python -m pip install -e .
echo Starting application...
python main.py
if errorlevel 1 (
    echo.
    echo An error occurred while running the application.
    echo Check the logs above for details.
    echo.
    pause
    exit /b 1
)
pause 