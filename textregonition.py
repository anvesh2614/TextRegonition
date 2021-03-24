import pytesseract as pt
import cv2
import regex as re
import preprocessingFun as pp
import Anglecheck as ac
pt.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#preproccessing steps
image = cv2.imread('3.jpg')

image = cv2.resize(image, None, fx=1.1, fy=1.1, interpolation=cv2.INTER_AREA)
image = ac.Angle(image)
originalImage = image
Grayimage = pp.get_grayscale(image)
image = pp.thresholding(Grayimage)






#detecting pancard number and DOB


pancardnumber = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
DOB = "^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$"
boxes = pt.image_to_data(image)
for a,b in enumerate(boxes.splitlines()):
    #print(b)
    if a != 0:
        b = b.split()
        if len(b) == 12:
            #print(a)
            #print(b[11])
            if re.match(DOB, b[11]):
                print("DOB match found",b[11])
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(originalImage, (x,y), (x+w, y+h), (0, 0, 255), 2)
            elif re.match(pancardnumber, b[11]):
                print("aadhar card match found", b[11])
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(originalImage, (x, y), (x + w, y + h), (0, 0, 255), 2)
            else:
                continue



cv2.imshow('result',originalImage)

cv2.waitKey(0)




