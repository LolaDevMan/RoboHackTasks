# Python code for Multiple Color Detection


import numpy as np
import cv2
 
#reading the image
img = cv2.imread('rubix.jpeg') 

#converting rgb to hsv
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow("xyz",hsvFrame)

#set range for red colour and define mask
red_lower = np.array([0, 50, 50], np.uint8)
red_upper = np.array([10, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

#set range for green colour and define mask
green_lower = np.array([36, 25, 25], np.uint8)
green_upper = np.array([86, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

#set range for blue colour and define mask
blue_lower = np.array([110, 50, 50], np.uint8)
blue_upper = np.array([130, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
	
#set range for yellow colour and define mask
yellow_lower = np.array([22,60,200], np.uint8)
yellow_upper = np.array([60,255,255], np.uint8)
yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)	

#set range for white colour and define mask
white_lower = np.array([0,0,0], np.uint8)
white_upper = np.array([0,100,128], np.uint8)
white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)

#set range for orange colour and define mask
orange_lower = np.array([1,190,200], np.uint8)
orange_upper = np.array([25,255,255], np.uint8)
orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

#morphological transform, dilation for each colour and bitwise and operator between img and mask determines to detect only that particular colour
kernal = np.ones((5, 5), "uint8")
	
#red mask
red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(img, img,
							mask = red_mask)
	
#green mask
green_mask = cv2.dilate(green_mask, kernal)
res_green = cv2.bitwise_and(img, img,
								mask = green_mask)
	
#blue mask
blue_mask = cv2.dilate(blue_mask, kernal)
res_blue = cv2.bitwise_and(img, img,
							mask = blue_mask)

#yellow mask
yellow_mask = cv2.dilate(yellow_mask, kernal)
res_yellow = cv2.bitwise_and(img, img,
								mask = yellow_mask)

#white mask
white_mask = cv2.dilate(white_mask, kernal)
res_white = cv2.bitwise_and(img, img,
								mask = white_mask)

#orange mask
orange_mask = cv2.dilate(orange_mask, kernal)
res_orange = cv2.bitwise_and(img, img,
								mask = orange_mask)

#contour for red colour
contours, hierarchy = cv2.findContours(red_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
for pic, contour in enumerate(contours):
	area = cv2.contourArea(contour)
	#print(area)
	if(area > 300):
		x, y, w, h = cv2.boundingRect(contour)
		img = cv2.rectangle(img, (x, y),
									(x + w, y + h),
									(0, 0, 255), 2)
			
		# cv2.putText(img, "Red Colour", (x, (y+50)),			#this line wont be visible as both background colour and the text colour are same, to view in different colour please comment this part and open the next commented line
		# 			cv2.FONT_HERSHEY_SIMPLEX, 0.8,			#(+50) is done for the y coordinate to include the colour name inside the frawn rectangle 
		# 			(0, 0, 255))

		cv2.putText(img, "Red Colour", (x, (y+50)),			#open this paragraph commented, and comment the above line to view "Red colour" being printed on the final window
					cv2.FONT_HERSHEY_SIMPLEX, 0.8,
					(255, 255, 255))

#contour for green colour
contours, hierarchy = cv2.findContours(green_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
for pic, contour in enumerate(contours):
	area = cv2.contourArea(contour)
	if(area > 300):
		x, y, w, h = cv2.boundingRect(contour)
		img = cv2.rectangle(img, (x, y),
									(x + w, y + h),
									(0, 255, 0), 2)
			
		cv2.putText(img, "Green Colour", (x, (y+50)),			#(+50) is done for the y coordinate to include the colour name inside the frawn rectangle 
					cv2.FONT_HERSHEY_SIMPLEX, 0.8,
					(0, 0, 255))

#contour for blue colour
contours, hierarchy = cv2.findContours(blue_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	area = cv2.contourArea(contour)
	if(area > 300):
		x, y, w, h = cv2.boundingRect(contour)
		img = cv2.rectangle(img, (x, y),
									(x + w, y + h),
									(255, 0, 0), 2)
			
		cv2.putText(img, "Blue Colour", (x, (y+50)),			#(+50) is done for the y coordinate to include the colour name inside the frawn rectangle 
						cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
						(0, 0, 255))

#contour for yellow colour
contours, hierarchy = cv2.findContours(yellow_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	area = cv2.contourArea(contour)
	if(area > 300):
		x, y, w, h = cv2.boundingRect(contour)
		img = cv2.rectangle(img, (x, y),
									(x + w, y + h),
									(0, 255, 255), 2)
			
		cv2.putText(img, "Yellow Colour", (x, (y+50)),			#(+50) is done for the y coordinate to include the colour name inside the frawn rectangle 
						cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
						(0, 0, 255))

#contour for white colour
contours, hierarchy = cv2.findContours(white_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	area = cv2.contourArea(contour)
	#print(area)
	if(1500 < area < 44600):										#current area is set such that the boundary of the cube and the overall boundary is enclosed in the rectange
		x, y, w, h = cv2.boundingRect(contour)
		img = cv2.rectangle(img, (x, y),
									(x + w, y + h),
									(25, 200, 180), 2)			#olive green rectangle drawn to differentiate from colour and background
			
		cv2.putText(img, "White Colour", (x, y+50),			#(+50) is done for the y coordinate to include the colour name inside the frawn rectangle 
						cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
						(0, 0, 255))

#contour for orange colour
contours, hierarchy = cv2.findContours(orange_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
	area = cv2.contourArea(contour)
	if(area > 300):
		x, y, w, h = cv2.boundingRect(contour)
		img = cv2.rectangle(img, (x, y),
									(x + w, y + h),
									(0, 128, 255), 2)
			
		cv2.putText(img, "Orange Colour", (x, (y+50)),			#(+50) is done for the y coordinate to include the colour name inside the frawn rectangle 
						cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
						(0, 0, 255))
			
#final window with required output
cv2.imshow("Rubic cube colour detection", img)

#escape sequence for closing the final window
cv2.waitKey() 
cv2.destroyAllWindows() 