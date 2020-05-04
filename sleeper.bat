@echo off
REM This is for opening python script by simple command "sleep <minutes>" [sleep is filename sleep.bat]

echo removing scheduled shutdown if exists.. 
Shutdown.exe -a

set /A minutes=%1
REM navigate to folder of this batch
cd /d %~dp0

py sleep.py %minutes%