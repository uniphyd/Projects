A WebApp that lets you transfer your college timetable to Google Calender.<br>
Language : Python

# Setup <br> 
Clone this repository first.
The project uses `Python 3.6` with the following packages.
- python-docx with `pip install python-docx` to install
- flask with `pip install flask` to install (Flask might throw and error, if it does `sudo apt-get install python-flask` should fix it )
- google-calender with `pip install --upgrade google-api-python-client oauth2client` to install. After installation, got to the [Google Calender] Python QUickstart to activate the API for your app, clicking on *Enable Google Calender API* should do this. During the process you will get a file called `credentials.json` place this in the root directory of your local version of this project. **Do not upload this file when contributing** 

After this you're all set! :sparkles:

# Running 
Currently everything runs seperately so this is divided into 3 files.
1. `calender.py` - Runs and creates the events. Type `python calender.py` to run.
2. `extract.py` - Extracts string text from a `.docx` file. Type `python extract.py` to rum.
3. `upload.py` - Starts server and deals with uploading a file. Type `python upload.py` to run.

The plan is to get everything started into a single file called `app.py` that starts the server and uses the other necessary files by exporting. I'd imagine we get to this soon.



