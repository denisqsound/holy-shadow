import cv2

# img = cv2.imread('img/1.jpg')
# cv2.imshow('privet', img)
# cv2.waitKey(10000)

# cap = cv2.VideoCapture('vid/traffic.mov')
cap = cv2.VideoCapture(0)

while True:
    err, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_filter = cv2.bilateralFilter(gray, 50, 5, 100)
    cv2.imshow(str(img.shape), img_filter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
