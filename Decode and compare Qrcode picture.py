from PIL import Image
from pyzbar.pyzbar import decode
dataB1 = decode(Image.open('B1.png')) #B1.png, B2.png is qrcode picture
dataB2 = decode(Image.open('B2.png'))
if(dataB1 == dataB2):
    print("same")
else:
    print("different")