# -*- coding: utf-8 -*-
import os
from flask import Flask, request, url_for, send_from_directory
from werkzeug import secure_filename
from predict import Predict
import database_Control
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>MNIST识别</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=上传>
    </form>
    '''


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


session=database_Control.database_ini()

myr = Predict()
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # result = 0
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            result = myr.predict(filename)
            database_Control.database_insert(session,file.filename,result)
            print(filename)
            return html + '<h2>'+ str(result) + '<h2>' +'<br><img src=' + file_url + '>'
    return html




if __name__ == '__main__':
   app.run('0.0.0.0',port=80)
