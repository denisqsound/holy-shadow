import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread("img/1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)[:3]

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 5, True)
    if len(approx) == 4:
        pos = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))

crop = gray[x1:x2, y1:y2]

text = easyocr.Reader(['en'])
text = text.readtext(crop)

print(text)
res = text[0][-2] + text[1][-2]
print(res)
final_image = cv2.putText(img, res, (y1, x2 + 60), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
final_image = cv2.rectangle(img, (y1, x1), (y2, x2), (0, 255, 0), 1)

pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
pl.show()
