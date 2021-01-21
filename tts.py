from gtts import gTTS
from playsound import playsound
from datetime import datetime
# import PyPDF2  as pypdf
# from wand.image import Image
# import os
from pdf2image import convert_from_path


from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

# audio = gTTS(text="tujhi aai ghaall",lang="mr",slow=False)
# audio.save("audio.mp3")
# playsound("audio.mp3")
#
# pdffile = open("rdpd.pdf",'rb')
# # creating a pdf reader object
# pdfReader = pypdf.PdfFileReader(pdffile)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# print(pageObj.extractText())
#
# # closing the pdf file object
# pdffile.close()


def add_timestamp_filename(filename):
    filename = filename.split(".")
    file = filename[0]
    file_ext = filename[1]
    now = datetime.now();
    timestamp = str(now.timestamp());
    timestamp = timestamp.replace(".", "")
    filename = file + timestamp + "." + file_ext

    return filename

#
# pdf_file = "p75.pdf"
#
# files = []
# with(Image(filename=pdf_file, resolution=500)) as conn:
#     for index, image in enumerate(conn.sequence):
#         image_name = os.path.splitext(pdf_file)[0] + str(index + 1) + '.png'
#         Image(image).save(filename=image_name)
#         files.append(image_name)


from pdf2image import convert_from_path
images = convert_from_path("p75.pdf", 500,poppler_path=r'D:\poppler-0.68.0\bin')
for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")