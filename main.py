import qrcode
import qrcode.image.svg
from PIL import Image

qr = qrcode.QRCode(version=1, box_size=50, border=2, )
colors = ["red", "orange", "blue", ]
file = input("Enter a url to create a qr code:  ")
name = input("Enter a name for your qrcode file: ")
qrname = str(name + ".png")

qr.add_data(file)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(qrname)

