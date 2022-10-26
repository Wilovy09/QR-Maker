import qrcode
from PIL import Image, ImageDraw
objeto = input('What will we make a qr code?\n¿A que le haremos un codigo qr?\n>>')
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(objeto)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color="white")
img.save('qr.png')