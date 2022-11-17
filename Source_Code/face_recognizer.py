import os

import cv2.cv2 as cv2


def face_recognizer():

    conf = []
    with open('names_id.txt', 'r') as file:
        data = file.read().replace('\n', '')

    names = ['None', str(data)]  # Add the names here ex ID: 1 = Jorge
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    font = cv2.FONT_ITALIC

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    minWidth = 0.1 * cap.get(3)
    minHeight = 0.1 * cap.get(4)

    for filename in os.listdir('./converted_videos_to_img/input/'):
        f = os.path.join('./converted_videos_to_img/input/', filename)
        img = cv2.imread(f)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minWidth), int(minHeight))
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id_, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            temp = confidence
            print(confidence)

            conf.append(float(temp))

            if confidence < 100:
                id_ = names[id_]

                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id_ = "Face Not Recognized"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id_), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            if float(temp) >= float(max(conf)):
                cv2.imwrite('static/output.jpg', img)



    # to clear the converted videos to img
    for filename in os.listdir('./converted_videos_to_img/input/'):
        f = os.path.join('./converted_videos_to_img/input/', filename)
        os.remove(f)