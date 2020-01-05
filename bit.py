import cv2
import numpy as np
img1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(img1, (100, 100), (250, 250), 255, -1)
cv2.imshow("Image 1", img1)
img2 = np.zeros((300, 300), dtype="uint8")
cv2.circle(img2, (150, 150), 90, 255, -1)
cv2.imshow("Image 2", img2)
A = cv2.bitwise_and(img1,img2)
cv2.imshow("AND operation",A)
B = cv2.bitwise_or(img1,img2)
cv2.imshow("OR operation",B)
k= cv2.bitwise_not(img1)
cv2.imshow("Not img1",k)
D = cv2.bitwise_not(img2)
cv2.imshow("Not img2",D)
cv2.waitKey(0)
cv2.destroyAllWindows()