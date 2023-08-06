# This script separate the train data between images with and without people. The images with people are labeled as 1 and the images without people are labeled as 0.

# Dependencies
import os
import pandas as pd
import shutil

# read the csv file
df = pd.read_csv('data/train.csv')

# for each row in the dataframe, find the image id and the label, and copy the image to the corresponding folder
for index, row in df.iterrows():
    # get the image id
    image_id = row['file_name']
    # get the label
    label = row['label']
    # get the source path
    src_path = os.path.join('data/train', image_id)
    # get the destination path
    dst_path = os.path.join('data/classes', str(label), image_id)
    # copy the image
    shutil.copy(src_path, dst_path)
    
# check the number of images in each folder
print('Number of images with people:', len(os.listdir('data/classes/1')))
print('Number of images without people:', len(os.listdir('data/classes/0')))
print('Total number of images: ', len(os.listdir('data/classes/1')) + len(os.listdir('data/classes/0')))
print('Total number of images in the original folder: ', len(os.listdir('data/train')))
      