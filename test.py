# Python code for Red Color Detection


import numpy as np
import cv2




# Start a while loop


# Reading the video from the
# webcam in image frames


# Convert the imageFrame in
# BGR(RGB color space) to
# HSV(hue-saturation-value)
# color space
imageFrame = cv2.imread("rubix.jpeg")
hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

# Set range for red color and
# define mask
red_lower = np.array([0, 50, 70])
red_upper = np.array([9, 255, 255])
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

kernel = np.ones((5, 5), "uint8")

# For red color
red_mask = cv2.dilate(red_mask, kernel)

# Creating contour to track red color
contours, hierarchy = cv2.findContours(red_mask,
									cv2.RETR_TREE,
									cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
	area = cv2.contourArea(contour)
	print(area)
	if(area > 44900):
		x, y, w, h = cv2.boundingRect(contour)
		imageFrame = cv2.rectangle(imageFrame, (x, y),
								(x + w, y + h),
								(0, 0, 255), 2)
		cv2.putText(imageFrame, "Red Colour", (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 1.0,
					(0, 0, 255))	
		
cv2.imshow("RED COLOR DETECTOR", imageFrame)
cv2.waitKey(0)