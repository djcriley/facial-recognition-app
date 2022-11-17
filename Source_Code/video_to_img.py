# Run the following command: python video_to_img.py
# train_sample_video directory ready to be filled with training data

import os
import cv2.cv2 as cv2
import math
import ntpath


def video_to_img():
    base_path = 'static/testing'
    i = 0

    for filename in os.listdir(base_path):
        file_name = ntpath.basename(filename).split('.')[0]
        if filename.endswith(".mp4"):
            converted_vid_2_img = os.path.join('converted_videos_to_img', 'input')

            if not os.path.isdir('converted_videos_to_img'):
                os.makedirs(converted_vid_2_img)

            print('Converting...')

            video_file = os.path.join(base_path, filename)
            capture = cv2.VideoCapture(video_file)
            frame_rate = capture.get(5)

            while capture.isOpened():
                frame_id = capture.get(1)
                ret, frame = capture.read()
                if not ret:
                    break
                if frame_id % math.floor(frame_rate) == 0:
                    width = int(frame.shape[1] * 1)
                    height = int(frame.shape[0] * 1)
                    dimensions = (width, height)
                    new_frame = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
                    print('loading...')

                    new_filename = '{}-{:03d}.png'.format(os.path.join(converted_vid_2_img, 'user_input'), i)
                    i += 1
                    cv2.imwrite(new_filename, new_frame)
            capture.release()
            print('End')
        else:
            continue
