import easyocr
import cv2
import numpy as np 
from rapidfuzz import process, fuzz
from constants import characters, normalized_characters
import re

reader = easyocr.Reader(['en']) 


def read_text_from_image(image):

    p1_region = image[80:125, 130:220] 
    p2_region = image[80:125, 385:480]
    
    p1_character_region = image[30:95, 90:220]  
    p2_chracter_region = image[30:85, 345:480]  

    cv2.imwrite("p1_region.png", p1_region)
    cv2.imwrite("p2_region.png", p2_region)
    cv2.imwrite("p1_character_region.png", p1_character_region)
    cv2.imwrite("p2_character_region.png", p2_chracter_region)

    p1_name = read_name(p1_region)
    p2_name = read_name(p2_region)

    p1_chracter_result = read_chracter(p1_character_region)
    p1_character = match_character(p1_chracter_result)
    p2_chracter_result = read_chracter(p2_chracter_region)
    p2_character = match_character(p2_chracter_result)

    print("P1 Name OCR: ", p1_name)
    print("P2 Name OCR: ", p2_name)
    print("P1 Character OCR: ", p1_chracter_result, " Matched: ", p1_character)
    print("P2 Character OCR: ", p2_chracter_result, " Matched: ", p2_character)

    return p1_name, p2_name, p1_character, p2_character

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def read_chracter(image):
    return reader.readtext(
        image, 
        detail=0, 
        text_threshold=0.7, 
        low_text=0.3, 
        paragraph=True,
        allowlist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ &.é/()"
    )[0]
    

def read_name(image):
    result = reader.readtext(
        image, 
        detail=0, 
        text_threshold=0.6, 
        low_text=0.3, 
        paragraph=True,
    )
    print("name result", result)

    return result[0] if result else ""

def crop_regions(image):
    h, w, _ = image.shape
    # Define regions for P1 and P2 characters (adjust coordinates as needed)
    # p1_region = image[80:125, 130:220]  # Example coordinates for P1
    # p2_region = image[80:125, 380:480]  # Example coordinates for P2
    # cv2.imwrite("p1_region5.png", p1_region)
    # cv2.imwrite("p2_region5.png", p2_region)

    p1c_region = image[30:95, 90:220]  # Example coordinates for P1
    p2c_region = image[30:85, 340:480]  # Example coordinates for P2
    cv2.imwrite("p1c_region5.png", p1c_region)
    cv2.imwrite("p2c_region5.png", p2c_region)

    
def match_character(ocr_text, threshold=50):
    text = normalize(ocr_text)
    match, score, idx = process.extractOne(text, normalized_characters, scorer=fuzz.WRatio)
    if score >= threshold:
        return characters[idx]  # Return original name for output
    else:
        return None


# print("Testing OCR and character matching...")
# image = cv2.imread("Found34.png")
# print(read_text_from_image(image))
# print(match_character("VILLAGER"))  # Test function