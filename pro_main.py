import cv2 #OpenCV for image processing
import time
from object_det import * #Object Detection lib
from picamera2 import Picamera2 #for taking camera input
from distance_estimation import distance_estimation #Distance estimation library
from OCR import OCR #For Text  Recognition
from gpiozero import Button #for buttons
from say import*

#initialising buttons
distance = Button(2) 
ocr = Button(3)

#size of the input image
normalSize = (640,480)
    
def main():
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": normalSize, "format": "RGB888"})
    picam2.configure(config)
    picam2.create_video_configuration()["controls"]['FrameDurationLimits']= (33333, 33333)
    picam2.start(show_preview=False)
    
    frame_count = 0
    starting_time = time.time()

    while True:
        frame_count += 1
        
        img = picam2.capture_array()
        img = cv2.resize(img,normalSize)
        
        if (frame_count % 1 == 0):
            
            result,boxes,class_names, data_list = detect(img)
            
            if (distance.is_pressed):
                data = distance_estimation(result,data_list)
                say(data)
                
            if (ocr.is_pressed):
                OCR(img)
                
            cv2.imshow("preview",img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        ending_time = time.time() - starting_time
        fps = frame_count/ending_time
    print(fps)            
    #cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

