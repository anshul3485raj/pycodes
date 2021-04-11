# import modules
import getpass
import eel
import pyqrcode
import png

# initialize eel
user = getpass.getuser()
eel.init(f"C://Users/{user}/Desktop/web")

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
