import cv2     #face_recognition is a library that is built from numpy, dlib, open cv and applying
# machine learning tools
import numpy as np
import face_recognition

mas = "/home/annu/Desktop/mars_attendance_sheet.txt" #this is our attendence sheet wherein, the code will mark the
# attendence of people ( note this adress is needed to be changed as per your computer system
sheet = open(mas, 'w')

friends = []

for i in range(1, 26):
    friends.append([0, 0, 0])
    friends[i - 1][0] = str(i)
    friends[i - 1][1] = False
    friends[i - 1][2] = face_recognition.load_image_file("/home/annu/Desktop/MaRS/0" + str(i) + ".jpeg")
    # this is where we make the data set of the students with there photos
    #what we have done is a manipulation of this data, i.e. we when initially making the dataset
    #named each photo with it's owners roll no. so whenever a photo is imported each element of above 2D array
    #is created which is easy enough, than individually typing the adress of photo , its owner in the code

friends_encodings = []

for i in range(len(friends)):
    friends_encodings.append(0)
    friends_encodings[i] = face_recognition.face_encodings(friends[i][2])[0] # here the array is converted to
    #an encoding that is machine readable and which the code utilises to compare 2 people as different



while True:
    cap = cv2.VideoCapture('http://192.168.0.123:8080/shot.jpg')# here the code takes the image encoding one by one
    # from the camera. if matched, marks attendence else take another screen shot
    ret, cam = cap.read()
    small_frame = cv2.resize(cam,(0,0), fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    cv2.imshow('Frame', cam) # this frame shows what is visible in a camera of corresponding ip containing phone
    cam_encodings = face_recognition.face_encodings(cam)
    for cam_encoding in cam_encodings:
        truefalsearray = face_recognition.compare_faces(friends_encodings, cam_encoding, tolerance=0.4)# this
        # basically is a list of binary elements that corresponding to each person's, image encoding, in the dataset
        # as in the picture taken. there may be more than one person too in the image
        for i, truefalse in enumerate(truefalsearray):
            if truefalse:
                cv2.imshow(friends[i][0], cam) # if an image matches any of one or more of the images of data set it
                # will show the corresponding test image that many number of times
                friends[i][1] = True

    if cv2.waitKey(1) & 0xFF == ord('q'): # pressing q will escape you from this camera and end the program for you
        # can see the attendence sheet then only
        break

for i in range(len(friends)):                # here the attendence sheet file if formated
    print(friends[i][0], friends[i][1])
    if friends[i][1]:
        sheet.write(str(i + 1) + "    " + "present\n")
    else:
        sheet.write(str(i + 1) + "    " + "absent\n")

cap.release()

sheet.close()
