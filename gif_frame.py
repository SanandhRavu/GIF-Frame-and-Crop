import os
import cv2

gif_path = input(GIF File Path: )
path = input(Destination Folder: )
gif = cv2.VideoCapture(gif_path)

count = 0
while True:
    ret, frame = gif.read()
    cv2.imwrite(os.path.join(path, "frame%d.jpg" % count), frame)
    count += 1

