import cv2.cv2 as cv2
import os


def add_new_face():
    base_path = 'static/uploads/'
    # This detects the face
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Make directory if "uploads" folder not exists
    if not os.path.isdir('face_dataset'):
        os.mkdir('face_dataset')

    i = 0
    for filename in os.listdir(base_path):
        if filename.endswith('.mp4'):
            face_dataset = os.path.join('face_dataset', filename)
            video_file = os.path.join(base_path, filename)
            capture = cv2.VideoCapture(video_file)

            while True:
                ret, img = capture.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # turn img to grey scale
                faces = face_detector.detectMultiScale(gray, 1.3, 5)

                for x, y, w, h in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw box around face
                    i += 1
                    cv2.imwrite("face_dataset/user.{0}.{1}.jpg".format(str(1), str(i)), gray[y:y + h, x:x + w])
                    # cv2.imshow('image', img)
                if i >= 30:         # 30 pictures, bump up for accuracy
                    break
        else:
            print("Wrong file type")

    # Close up everything
    # cv2.destroyAllWindows()
