# this script is used to test the annotations of the yolov8 model

# import the necessary packages
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# image path
IMAGES_PATH = "./data/compressed_yolov8/train/images"
# annotation path
ANNOTATIONS_PATH = "./data/compressed_yolov8/train/labels"

# get the first image that is available
id = random.randint(0, len(os.listdir(IMAGES_PATH)))
image = os.listdir(IMAGES_PATH)[id]
# get the corresponding annotation
annotation = os.listdir(ANNOTATIONS_PATH)[id]

print("Image: {}".format(image))
print("Annotation: {}".format(annotation))

# draw the image
image = Image.open(os.path.join(IMAGES_PATH, image))
draw = ImageDraw.Draw(image)

# read the annotation
annotation = open(os.path.join(ANNOTATIONS_PATH, annotation)).read().splitlines()

# loop over the annotation
for ann in annotation:
    ann = ann.split()
    # get the class, x, y, w, h
    cls, x, y, w, h = ann[0], float(ann[1]), float(ann[2]), float(ann[3]), float(ann[4])
    # get the top left and bottom right coordinates
    tl = (int((x - w / 2) * image.size[0]), int((y - h / 2) * image.size[1]))
    br = (int((x + w / 2) * image.size[0]), int((y + h / 2) * image.size[1]))
    # draw the rectangle
    draw.rectangle([tl, br], outline="red", width=5)
    # draw the class
    draw.text(tl, cls, fill="red", font=ImageFont.truetype("arial.ttf", 15))
    
# show the image
plt.imshow(np.asarray(image))
plt.show()

