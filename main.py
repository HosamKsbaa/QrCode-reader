import qrcode
import cv2

img = qrcode.make('http://www.baidu.com')
img.save("d.jpg")

d=cv2.QRCodeDetector()
val,points,st = d.detectAndDecode(cv2.imread("d.jpg"))
print(val)