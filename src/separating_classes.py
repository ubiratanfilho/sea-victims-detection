# This script separate the train data between images with and without people. The images with people are labeled as 1 and the images without people are labeled as 0.

# Dependencies
import os
import pandas as pd
import shutil

def separate_data(in_path: str, out_path: str, csv_path: str):
    # read the csv file
    df = pd.read_csv(csv_path)

    # for each row in the dataframe, find the image id and the label, and copy the image to the corresponding folder
    for index, row in df.iterrows():
        # get the image id
        image_id = row['file_name']
        # get the label
        label = row['label']
        # get the source path
        src_path = in_path + '/' + image_id
        # get the destination path
        dst_path = out_path + '/' + str(label) + '/' + image_id
        # copy the image
        shutil.copy(src_path, dst_path)
        
    # check the number of images in each folder
    n_1 = len(os.listdir(out_path + '/1'))
    n_0 = len(os.listdir(out_path + '/0'))
    print('Number of images with people:', n_1)
    print('Number of images without people:', n_0)
    print('Total number of images:', n_1 + n_0)
    print('Total number of images in the original folder:', len(os.listdir(in_path)))
      
# define the paths
in_path = '../data/compressed/images/train'
out_path = '../data/compressed/separated/train'
csv_path = '../data/compressed/annotations/train_annotations.csv'

# call the function
separate_data(in_path, out_path, csv_path)