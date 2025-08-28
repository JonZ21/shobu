import cv2
import pytesseract
import numpy as np

def detect_end(frame, index = ""):
    # Template matching is based on raw pixel data. 
    crop = crop_frame(frame)
    modified_frame = modify_frame(crop) 
    template = cv2.imread("template.png", cv2.IMREAD_GRAYSCALE)
    res = cv2.matchTemplate(modified_frame, template, cv2.TM_CCORR_NORMED)

    loc = np.where(res >= 0.9)  # 0.8 = threshold
    if len(loc[0]) > 0:
        print(index + " End screen detected!" + str(res.max()))
        return True
    return False


def use_OCR(frame, index = ""):
    modified_frame = modify_frame(frame)
    config = "--psm 11"  # Treat image as a single text line

    text = pytesseract.image_to_string(modified_frame, config=config).lower()
    print(index + " OCR RESULTS: ", text)
    cv2.imwrite("crop"+index+".png",modified_frame)
    return text 

def modify_frame(frame):
    # Crop bottom-right corner (adjust coordinates as needed)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    scale_factor = 2
    thresh = cv2.resize(thresh, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    return thresh


def crop_frame(frame):
    h, w, _ = frame.shape
    # crop = frame[h-40:h-10, w-100:w-10] # crop for the save replay area
    crop = frame[280:320, 100:180] # crop for 'out at' P1 ( p2 wins) 
    return crop

def is_player_2_winner(frame):
    h, w, _ = frame.shape
    crop = frame[280:320, 350:530] # Player 2 wins if this crop gets "---", meaning they were not out at a time
    modified_frame = modify_frame(crop)
    template = cv2.imread("nullTimeOut.png", cv2.IMREAD_GRAYSCALE)
    res = cv2.matchTemplate(modified_frame, template, cv2.TM_CCORR_NORMED)

    loc = np.where(res >= 0.9) 
    if len(loc[0]) > 0:
        print("Player 2 wins detected!" + str(res.max()))
        return True
    print("Player 1 wins detected!")
    return False


# count = 0
# for i in range(9):
#     index = str(i+1)
#     frame = cv2.imread("end"+index+".png")
#     text = useOCR(frame,index)
#     if "repla" in text or "save" in text:
#         print(index + "End screen detected!")
#         count += 1
#     else:
#         print(index + "NOT detected")
# print("total detections: ", count)


# count = 0 
# for i in range(197):
#     frame = cv2.imread("capture" + str(i+1) + ".png")
#     index = str(i+1)
#     if useTemplate(frame, index):
#         count += 1


# bruh = cv2.imread("Found4.png")
# modified_frame = modify_frame(bruh)
# cv2.imwrite("template2.png", modified_frame)
# detectEnd(bruh)


# frame = cv2.imread("Found5.png")
# is_player_2_winner(frame)