# About
Python command line application to download songs/videos using YouTube.

## Download Options
- By song title(s) / search string
- By link (song/playlist)
- By CSV (simple) - CSV/database location (if not detected at default location), all songs
- By CSV (advanced) - CSV/database location, start index, end index, output location, simultaneous thread count

# Steps to download songs
- Use 'https://www.tunemymusic.com/transfer/youtube-to-file' to get CSV from Youtube/Spotify etc. playlist
- Download the CSV file to any local folder (default: <repository_location>/database)
- Install python 3.9+ from 'https://www.python.org/downloads/'
- (recommended) Make a virtual env (python -m venv env)
- (recommended) Activate virtual env (VS code -> Select interpreter or start env/Scripts/activate.bat)
- Install required modules (pip install -r requirements.txt)
- Run main.py (python ytube_console.py)
- Enter required data
- Logs file for status : (local path)/logs.log

# Steps to generate executable file
- Install python 3.9+ from 'https://www.python.org/downloads/'
- (recommended) Make a virtual env (python -m venv env)
- (recommended) Activate virtual env (VS code -> Select interpreter or start env/Scripts/activate.bat)
- Install required modules (pip install requirements.txt)
- Generate executable using the command (pyinstaller ytube_console.py --onefile)
- Executable generated at location (<repository_location>\dist\ytube_console.exe)
