echo off
call venv\scripts\activate
rem pytest -s -v -m "ui" --html .\Reports\LoginReport.html .\testCases\test_Home_Page.py --browser chrome --headless -n3
rem pytest -s -v -m "smoke" --html .\Reports\TableHandle.html .\testCases\test_Handle_Table.py --browser chrome -n3
pytest -s -v -m "smoke" --html .\Reports\LinkTest.html .\testCases\test_Links.py --browser chrome -n3
pause