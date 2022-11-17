# To run open your command line and enter: python detect_face.py
# WARNING: Must have run video_to_img.py before running this file

import ntpath
import os.path
import cv2 as cv2
from mtcnn import MTCNN
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

root_dir = 'converted_videos_to_img'
i = 0

for filename in os.listdir(root_dir):
    file_name = ntpath.basename(filename).split('.')[0]
    cropped_videos = os.path.join(root_dir, file_name)
    frame_images = [x for x in os.listdir(cropped_videos) if os.path.isfile(os.path.join(cropped_videos, x))]

    faces_path = os.path.join(cropped_videos, 'faces')
    os.makedirs(faces_path)

    for frames in frame_images:
        file_name_frames = ntpath.basename(frames).split('.')[0]
        detector = MTCNN()
        image = cv2.cvtColor(cv2.imread(os.path.join(cropped_videos, frames)), cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(image)

        for faces in faces:
            bounding_box = faces['box']
            confidence = faces['confidence']
            if len(faces) < 2 or confidence > 0.95:

                margin_x = bounding_box[2] * 0.2
                margin_y = bounding_box[3] * 0.2

                x1 = int(bounding_box[0] - margin_x)
                if x1 < 0:
                    x1 = 0

                x2 = int(bounding_box[0] + bounding_box[2] + margin_x)
                if x2 > image.shape[1]:
                    x2 = image.shape[1]

                y1 = int(bounding_box[1] - margin_y)
                if y1 < 0:
                    y1 = 0

                y2 = int(bounding_box[1] + bounding_box[3] + margin_y)
                if y2 > image.shape[0]:
                    y2 = image.shape[0]

                print(x1, y1, x2, y2)
                crop_image = image[y1:y2, x1:x2]

                new_filename = '{}-{:02d}.png'.format(os.path.join(faces_path, file_name_frames), i)
                i += 1
                cv2.imwrite(new_filename, cv2.cvtColor(crop_image, cv2.COLOR_RGB2BGR))
            else:
                print('Face not detected..')
