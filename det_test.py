from object_det import *
from distance_estimation import *
import cv2
import os
files = [f for f in os.listdir("/home/pi4/ETA/imagesnew/") if os.path.isfile(f)]

print(os.listdir("/home/pi4/ETA/imagesnew/"))
for f in os.listdir("/home/pi4/ETA/imagesnew/"):
	img=cv2.imread("/home/pi4/ETA/imagesnew/"+f)
	img = cv2.resize(img, (640,480))
	img, rectangles, class_names, data_list = detect(img)
	
	distance_estimation(img,data_list)
	
	cv2.imshow(f"{f}", img)
	cv2.imwrite(f"/home/pi4/ETA/imagesnew/detected/{f}", img)
	cv2.waitKey(0)
cv2.destroyAllWindows()
