@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5355266750:AAFF5RCzS8zdWHIMR2v9Q-3DhEuWU5qEKfc

python bot_telegram.py

pause