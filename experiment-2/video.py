import cv2
from deepface import DeepFace

def third(path):
    print(path)
    cam = cv2.VideoCapture(path)

    # frame_per_second = cam.get(cv2.CAP_PROP_FPS)
    ret, frame = cam.read()
    if ret ==True:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.1,4)
        res = type(faces) is tuple
        if res==False:
            print('Face Detected')
        else:
            print('Analyzing without face')
    
    result = DeepFace.analyze(frame,actions=['emotion'], enforce_detection=False)

    if result[0]['emotion']['happy'] > result[0]['emotion']['sad']:
        return ("Video Analysis: Video is positive")
    else:
        return ("Video Analysis: Video is negative")
