import numpy as np
import cv2
import serial
import time

flag1,flag2,flag3,c1=0,0,0,0

linecolor = (100, 215, 255)

# color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
#               'white': [[180, 18, 255], [0, 0, 231]],
#               'red1': [[180, 255, 255], [159, 50, 70]],
#               'red2': [[9, 255, 255], [0, 50, 70]],
#               'green': [[89, 255, 255], [36, 50, 70]],
#               'blue': [[128, 255, 255], [90, 50, 70]],
#               'yellow': [[35, 255, 255], [25, 50, 70]],
#               'purple': [[158, 255, 255], [129, 50, 70]],
#               'orange': [[24, 255, 255], [10, 50, 70]],
#               'gray': [[180, 18, 230], [0, 0, 40]]}

lwr_red = np.array([0, 50, 70])
upper_red = np.array([9, 255, 255])

lwr_green = np.array([68, 142, 74])
upper_green = np.array([88, 162, 154])

lwr_violet = np.array([108,193,52])
upper_violet = np.array([131,255,159])

lwr_pink = np.array([161,134,176])
upper_pink = np.array([179,171,255])

lwr_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])
frame = cv2.imread("rubix.jpeg")

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.inRange(hsv, lwr_red, upper_red)
mask = cv2.dilate(mask, kernel, iterations=1)
res = cv2.bitwise_and(frame, frame, mask=mask)
cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
center = None

green_mask = cv2.inRange(hsv, lwr_green, upper_green)
violet_mask = cv2.inRange(hsv, lwr_violet, upper_violet)
pink_mask = cv2.inRange(hsv, lwr_pink, upper_pink)
red_mask = cv2.inRange(hsv, lwr_red, upper_red)
cv2.imshow("mask", mask)
c = max(cnts, key=cv2.contourArea)
area = cv2.contourArea(c)
print(area)
