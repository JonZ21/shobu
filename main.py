import os
import subprocess
import cv2
import time


from detect_end import detect_end, is_player_2_winner
from scrape_results import read_text_from_image
from upload_match import upload_match

VIDEO_DEVICE = "/dev/video0"

def main_loop():
    cap = cv2.VideoCapture(VIDEO_DEVICE)
    if not cap.isOpened():
        print("Failed to open video device!")
        return
    count = 236
    found_count = 0 
    in_end_screen = False
    saving_results = False
    while True:
        ret, frame = cap.read()
        if not ret:
            continue  # skip if frame not ready

        if not saving_results:
            if detect_end(frame):
                print("end detected")
                if found_count >= 3 and not in_end_screen:
                    in_end_screen = True
                    found_count = 0
                else:  
                    found_count += 1

            else:
                print("no end detected")
                in_end_screen = False
            
        if in_end_screen:
            print("End detected! Saving frame or taking action...")
            saving_results = True
            # Save the frame or trigger your upload/log
            cv2.imwrite("EndScreen.png", frame)
            results = read_text_from_image(frame)
            p2_winner = is_player_2_winner(frame)
            print("Extracted Results: ", results, " Player 2 Winner: ", p2_winner)
            # input("Press Enter to upload to Supabase...")  # Wait for user confirmation
            upload_match(
                results[0], 
                results[1], 
                results[2], 
                results[3], 
                results[1] if p2_winner else results[0]
            )
            time.sleep(120)
            saving_results = False

    
            

        # cv2.imwrite("capture" + str(count) + ".png", frame)
        # print(f"Screenshot saved as capture{count}.png")
        # count += 1
        # time.sleep(5)  # Wait 5 seconds before next screenshot
    cap.release()

if __name__ == "__main__":
    main_loop()

# VIDEO_DEVICE = "/dev/video0"   #
# TMP_FILE = "/home/jon/smash_project/tmp_recording.mp4"

# def record_video():
#     # Record 10s of video
#     cmd = [
#         "ffmpeg",
#         "-y",              # overwrite if exists
#         "-t", "10",        # duration
#         "-f", "v4l2",      # capture from video4linux2
#         "-i", VIDEO_DEVICE,
#         TMP_FILE
#     ]
#     subprocess.run(cmd)
# def detect_end_in_video():
#     cap = cv2.VideoCapture(TMP_FILE)
#     found = False
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         if useTemplate(frame):  # update useTemplate to return True/False
#             found = True
#             break
#     cap.release()
#     return found

# def main_loop():
#     while True:
#         print("Recording video...")
#         record_video()
#         print("Analyzing video for end screen...")
#         if detect_end_in_video():
#             print("End detected! Keeping video.")
#             # TODO: save/rename file, upload, log, etc.
#         else:
#             os.remove(TMP_FILE)
#             print("No end detected. Deleted.")

# if __name__ == "__main__":
#     main_loop()