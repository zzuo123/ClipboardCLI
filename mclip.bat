@echo off
CALL venv\Scripts\activate
@py.exe mclip.py %*
::CALL venv\Scripts\deactivate
@pause