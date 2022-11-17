import os

from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

from add_new_face import add_new_face
from face_recognizer import face_recognizer
from training_face_detector import training_face_detector
from video_to_img import video_to_img

UPLOAD_FOLDER = 'static/uploads/'
TESTING_UPLOAD = 'static/testing/'
ALLOWED_EXTENSIONS = {'mp4', 'pdf', 'png', 'jpeg', 'jpg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TESTING_UPLOAD'] = TESTING_UPLOAD
app.config["SECRET_KEY"] = "secret123"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    # Make directory if "uploads" folder not exists
    if not os.path.isdir('static/uploads/'):
        os.mkdir('static/uploads/')

    if request.method == 'POST':
        # check if the post request has the files part
        file = request.files['File']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        form_data = request.form
        file2 = open('names_id.txt', 'w')
        file2.write(form_data.get("Name"))
        file2.close()

        add_new_face()
        training_face_detector()

        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return redirect('/testing')


@app.route('/testing')
def upload_form2():
    return render_template('upload_testing.html')


@app.route('/testing', methods=['POST'])
def upload_testing():
    # Make directory if "uploads" folder not exists
    if not os.path.isdir('static/testing/'):
        os.mkdir('static/testing/')

    if request.method == 'POST':
        # check if the post request has the files part
        file = request.files['File']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(TESTING_UPLOAD, filename))

        video_to_img()
        face_recognizer()

        os.remove(os.path.join(app.config['TESTING_UPLOAD'], filename))
        return render_template('display.html')


if __name__ == "__main__":
    app.config["SECRET_KEY"] = "secret123"
    app.run(host='0.0.0.0', port=5000, debug=True)
