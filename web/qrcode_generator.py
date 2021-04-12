# import modules
import getpass
import eel
import pyqrcode
import png
import os
# initialize eel
user = getpass.getuser()
current_directory = os.getcwd()
eel.init(current_directory)


# qrcode


@eel.expose
def qrcode_generator(url):
    # Generate the QRcode
    url = pyqrcode.create(url)
    # create and save the png file name
    img = url.png('myqr.png', scale=6)
    return img


# start the eel windows
eel.start("index.html", size=(1000, 600))
