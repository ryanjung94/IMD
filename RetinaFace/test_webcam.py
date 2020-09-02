import cv2
import sys
import numpy as np
import datetime
import os
import glob
from RetinaFace.retinaface import RetinaFace

gpuid = 0
detector = RetinaFace('./model/R50', 0, gpuid, 'net3')

thresh = 0.8
scales = [1024, 1980]

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while (True):
    ret, img = cap.read()
    faces, landmarks = detector.detect(img, thresh, scales=[1.0, 1.0], do_flip=False)

    if True:
        for i in range(faces.shape[0]):
            box = faces[i].astype(np.int)
            color = (0, 0, 255)
            # cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), color, 2)
            cv2.putText(img, 'Man', (box[0], box[1]-2), 0, 1, [0,0,0], thickness=3, lineType=cv2.FONT_HERSHEY_SIMPLEX)
            if landmarks is not None:
                landmark5 = landmarks[i].astype(np.int)
                for l in range(landmark5.shape[0]):
                    color = (0, 0, 255)
                    if l == 0 or l == 3:
                        color = (0, 255, 0)
                    cv2.circle(img, (landmark5[l][0], landmark5[l][1]), 1, color, 2)
    cv2.imshow('Face Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
