@echo off
SET ORIGINAL=%CD%
cd :: put the directory of this folder here!
CALL venv\Scripts\activate
@py.exe mclip.py %*
CALL venv\Scripts\deactivate
cd %ORIGINAL%
@pause