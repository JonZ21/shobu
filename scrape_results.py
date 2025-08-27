import easyocr
import cv2

reader = easyocr.Reader(['en']) 


def crop_frame(frame):
    h, w, _ = frame.shape
    # crop = frame[h-40:h-10, w-100:w-10] # crop for the save replay area
    crop = frame[10:150,100:w-100] # crop for 'out at' P1 ( p2 wins) 
    return crop

def read_text_from_image(image):
    result = reader.readtext(image)
    print("result", result)

image = cv2.imread("Found3.png")
cropped = crop_frame(image)
cv2.imwrite("cropped.png", cropped)
read_text_from_image(cropped)