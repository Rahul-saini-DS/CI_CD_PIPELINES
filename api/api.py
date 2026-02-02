import time
import os
import sys
from flask import Flask

def get_static_folder():
    """
    Determine the correct path to the 'build' folder.
    - If running as an .exe (frozen), use the temporary folder sys._MEIPASS.
    - If running as a script (dev), use the normal relative path '../build'.
    """
    if getattr(sys, 'frozen', False):
        # Running as compiled .exe
        # The 'build' folder is inside the temp directory because of --add-data "build;build"
        base_path = sys._MEIPASS
        return os.path.join(base_path, 'build')
    else:
        # Running as normal python script
        return '../build'

# Calculate the folder path once on startup
static_folder_path = get_static_folder()

# Initialize Flask with the dynamic path
app = Flask(__name__, static_folder=static_folder_path, static_url_path='/')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

# You need this block so the EXE starts the server when double-clicked!
if __name__ == '__main__':
    # Threaded=True is good for basic testing/demos
    app.run(host='0.0.0.0', port=5000, debug=False)
