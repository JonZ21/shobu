import os
import subprocess
import cv2
import time


from detect_end import useTemplate 

VIDEO_DEVICE = "/dev/video0"

def main_loop():
    cap = cv2.VideoCapture(VIDEO_DEVICE)
    if not cap.isOpened():
        print("Failed to open video device!")
        return
    count = 73
    found_count = 0 
    while True:
        ret, frame = cap.read()
        if not ret:
            continue  # skip if frame not ready

        if useTemplate(frame):
            print("End detected! Saving frame or taking action...")
            # Save the frame or trigger your upload/log
            cv2.imwrite("Found"+str(found_count)+".png", frame)
            found_count += 1
            # Could also save a small video clip here if needed
            continue

         # Wait for user input to save the current frame
        # user_input = input("Press Enter to save current frame, or type 'q' to quit: ")
        # if user_input == "y":
        #     cv2.imwrite("capture" + str(count) + ".png", frame)
        #     print("saved")
        #     count += 1
        # elif user_input.lower() == "q":
        #     print("Exiting loop.")
        #     break

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