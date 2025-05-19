echo off
call venv\scripts\activate
pytest -s -v -m "ui" --html .\Reports\LoginReport.html .\testCases\test_Home_Page.py --browser chrome --headless -n3
pause