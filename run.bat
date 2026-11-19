@echo off
title Amazon Agent Gatekeeper
echo ========================================================
echo       Amazon Agent Gatekeeper - Starting App
echo ========================================================
echo.

REM Check if Anaconda's streamlit is available
if exist "C:\Users\Anuja\anaconda3\Scripts\streamlit.exe" (
    echo Using Anaconda Streamlit...
    "C:\Users\Anuja\anaconda3\Scripts\streamlit.exe" run app.py
    goto end
)

REM Fallback to system streamlit
where streamlit >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo Using system Streamlit...
    streamlit run app.py
    goto end
)

REM Fallback to python -m streamlit
echo Trying python -m streamlit...
python -m streamlit run app.py

:end
pause
