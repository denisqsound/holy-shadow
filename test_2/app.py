from PIL import Image
import pytesseract
import cv2
import os
from matplotlib import pyplot as pl

image = 'img/2.jpg'

preprocess = "thresh"

# загрузить образ и преобразовать его в оттенки серого
image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Дополнительная обработка
# img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
# edges = cv2.Canny(img_filter, 30, 200)
# cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cont = imutils.grab_contours(cont)
# cont = sorted(cont, key=cv2.contourArea, reverse=True)[:10]
# pos = None
# for c in cont:
#     approx = cv2.approxPolyDP(c, 20, True)
#     if len(approx) == 4:
#         pos = approx
#         break
#
# mask = np.zeros(gray.shape, np.uint8)
# new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
# bitwise_img = cv2.bitwise_and(image, image, mask=mask)
# (x, y) = np.where(mask == 255)
# (x1, y1) = (np.min(x), np.min(y))
# (x2, y2) = (np.max(x), np.max(y))
#
# crop = gray[x1:x2, y1:y2]

# проверьте, следует ли применять пороговое значение для предварительной обработки изображения
if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# если нужно медианное размытие, чтобы удалить шум
elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

# сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# показать выходные изображения
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)

pl.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
pl.show()

input('pause…')

