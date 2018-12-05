import json #, os
#from gui import *
#from bluetooth import *
import time
#import picamera
import os
import cv2
import shutil
#from imutils.video import VideoStream
from imutils import paths
import face_recognition
#import argparse
import pickle



def face_registration(name, amount_pictures, camera):
    
    path = '/home/pi/Documenten/peno3/pi-face-recognition/dataset/'+name
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    camera.resolution= (1280,720)
    camera.start_preview()
    
    
        
    for picture in range(0,amount_pictures):
        for i in range(3,0,-1):
            camera.annotate_text_size = 120
            camera.annotate_text = str(i)
            time.sleep(1)
        camera.annotate_text = " "
        camera.capture(path+'/'+name+str(picture)+'.jpg')
        time.sleep(1)
        
        
    camera.stop_preview()
    camera.close()
    print("stop preview")
    
def learn_faces():

    # grab the paths to the input images in our dataset
    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images("/home/pi/Documenten/peno3/pi-face-recognition/dataset"))

    # initialize the list of known encodings and known names
    knownEncodings = []
    knownNames = []

    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(i + 1,
                    len(imagePaths)))
            name = imagePath.split(os.path.sep)[-2]

            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb,
                    model="hog")

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)

            # loop over the encodings
            for encoding in encodings:
                    # add each encoding + name to our set of known names and
                    # encodings
                    knownEncodings.append(encoding)
                    knownNames.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("/home/pi/Documenten/peno3/pi-face-recognition/encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()

