import cv2.cv2 as cv2
import numpy as np
from PIL import Image
import os


def training_face_detector():
    # path for faces image
    file_path = 'face_dataset'

    recognizer = cv2.face.LBPHFaceRecognizer_create()   # Recognizer included with opencv
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")     # Help detect face features

    # This function will take the photos in path and
    # return 2 arrays ids and faces to train our recognizer
    def get_img_labels(file_path):
        imagePaths = []

        for files in os.listdir(file_path):
            imagePaths.append(os.path.join(file_path, files))

        faceSamples = []
        face_id = []

        for imagePaths in imagePaths:
            PIL_img = Image.open(imagePaths).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePaths)[-1].split(".")[1])
            faces = face_cascade.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                face_id.append(id)

        return faceSamples, face_id

    faces, ids = get_img_labels(file_path)
    recognizer.train(faces, np.array(ids))  # Train our recognizer
    recognizer.write('trainer.yml')     # Save the model into trainer.yml

    file_path = './face_dataset/'
    for file in os.listdir(file_path):
        f = os.path.join('./face_dataset/', file)
        os.remove(f)
