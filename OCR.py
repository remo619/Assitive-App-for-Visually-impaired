#from PIL import Image
import pytesseract
import cv2
import numpy as np
import easyocr
import pyttsx3
import subprocess

engine = pyttsx3.init()
engine.setProperty('rate',100)
#voices=engine.getProperty('voices')


#img = cv2.imread("/home/pi4/read.png")
img = cv2.imread("/home/pi4/Downloads/IMG20220725150236.jpg")
img = cv2.resize(img, (640,480))
#text = pytesseract.image_to_string(img, config='-l eng --oem 3 --psm 12')
#print(text)

def OCR(img):
    #text_img = np.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #blur = cv2.bilateralFilter(gray, 11,7,7)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    ret, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(thresh, config = '')
    print(text)
    #exit_code = subprocess.check_call("./speech.sh '%s'" %text, shell=True)
    
    engine.say(str(text))
    engine.runAndWait()


