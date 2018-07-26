from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_filer():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename)) # replace f.filename with your own file name if you want all uploaded files to have the same filename
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)