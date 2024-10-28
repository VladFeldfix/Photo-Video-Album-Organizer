set "currentDirectory=%cd%
pyinstaller --distpath %currentDirectory% -i favicon.ico --onefile Photo-Video-Album-Organizer.py
pause