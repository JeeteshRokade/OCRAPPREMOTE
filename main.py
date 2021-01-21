from doctest import debug
import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import cv2
import pytesseract
from gtts import gTTS
import os
from io import BytesIO
from datetime import datetime
from playsound import playsound
from pdf2image import convert_from_path

mp3_fp = BytesIO()

#pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

msg="Please select a file"
app = Flask(__name__)
UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','PNG'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#
# window_name = 'image'
# path = "images/test.png"
# image = cv2.imread(path)
# cv2.imshow(window_name,image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

language = 'en'

def ocr_core(file):
    global text
    """
    This function will handle the core OCR processing of images.
    """
    if file:
        image = cv2.imread(file,1)
        text = pytesseract.image_to_string(image)

    return text


# print(ocr_core(image))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_to_image(filepath):
    images = convert_from_path(filepath, 500, poppler_path=r'D:\poppler-0.68.0\bin')
    for i, image in enumerate(images):
        fname = 'image' + str(i) + '.png'
        image.save(fname, "PNG")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global langauage
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            return render_template("home.html",msg = msg )
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            # flash('No selected file')
            return render_template("home.html",msg = msg )
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = add_timestamp_filename(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path = UPLOAD_FOLDER + filename
            text = ocr_core(file_path)
            audiopath = convert_to_audio(text)
            print(audiopath," | ",file_path)
            return render_template("home.html",msg="File selected",text=text,img_src = file_path,audiopath=audiopath)


def add_timestamp_filename(filename):
    filename = filename.split(".")
    file = filename[0]
    file_ext = filename[1]
    now = datetime.now();
    timestamp = str(now.timestamp());
    timestamp = timestamp.replace(".", "")
    filename = file + timestamp + "." + file_ext

    return filename


def convert_to_audio(text):
    audio = gTTS(text=text, lang="en", slow=False)
    audiofilename = add_timestamp_filename("audio.mp3")
    audio.save(os.path.join(app.config['UPLOAD_FOLDER'], audiofilename))
    audiopath = "static/"+audiofilename
    # playsound(os.path.join(app.config['UPLOAD_FOLDER'], "audio.mp3"))

    return audiopath







if __name__ == "__main__":
    app.run()

