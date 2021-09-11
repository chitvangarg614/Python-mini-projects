import qrcode
data=input("Enter link to generate qr code")
img= qrcode.make(data)
img.save("LinkedIn.jpg")

import cv2
det= cv2.QRCodeDetector()
retval,points, straight_qrcode= det.detectAndDecode(cv2.imread("LinkedIn.jpg"))
print(retval)