'''
===================================================
           Frame Extraction from Video
===================================================
Program To Read video and Extract Frames 
'''

path_of_video="/home/tanmoydas1997/Desktop/s1_an_1.avi"

import cv2 
import os  
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        if not os.path.exists("Frames"):
            os.makedirs("Frames")
        # Saves the frames with frame-count 
        cv2.imwrite("Frames/frame%d.jpg" % count, image) 
  
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(path_of_video) 
