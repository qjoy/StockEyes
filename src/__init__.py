import cv2
# import numpy as np
# import matplotlib
# import numpy

img = cv2.imread("/Users/alex_xq/PycharmProjects/OpenCVTest/src/asset/src601901.png")
# hsv = cv2.cvtColor("/Users/alex_xq/PycharmProjects/OpenCVTest/src/asset/xueqiu.png", cv2.COLOR_BGR2HSV)
# lower_red = np.array([30, 150, 50])
# upper_red = np.array([255, 255, 180])
# mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow("Image", img)

cv2.waitKey()

cv2.destroyAllWindows()

