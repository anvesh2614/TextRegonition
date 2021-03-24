import pytesseract as pt
import cv2
import regex as re
import preprocessingFun as pp

def Angle(image):
    osd = pt.image_to_osd(image)
    angle = re.search('(?<=Rotate: )\d+', osd).group(0)
    print("angle: ", angle)
    if int(angle) == 0:
        return image


    else:
        image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
        return image
