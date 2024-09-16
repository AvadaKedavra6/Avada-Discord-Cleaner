@echo off
echo [ADC] Installing required Python packages...
pip install -r requirements.txt

echo [ADC] Launching...
python main.py

pause