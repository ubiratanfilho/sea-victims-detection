# JSON Data to CSV
## This code is used to convert JSON data to CSV format

import json
import pandas as pd
import os

def json_images_to_csv(json_path: list, csv_path: str):
    """
    This function is used to convert JSON data to CSV format
    
    Arguments:
        json_path: list
            Path to JSON file
        csv_path: str
            Path to CSV file
    """
    # elif _type == 'images':
    #     data = json_data['images']
        
    #     df = pd.DataFrame(data)
        
    #     # now expand the column 'source'
    #     df = pd.concat([df.drop(['source'], axis=1), df['source'].apply(pd.Series)], axis=1)
    #     # now expand the column 'meta'
    #     df = pd.concat([df.drop(['meta'], axis=1), df['meta'].apply(pd.Series)], axis=1)
    # else:
    #     raise ValueError('Invalid type')
    # df.to_csv(csv_path, index=False)


def json_annotations_to_csv(json_paths: list, csv_path: str):
    """
    This function is used to convert JSON data to CSV format
    
    Arguments:
        json_path: list
            Path to JSON file
        csv_path: str
            Path to CSV file
    """
    df_all = pd.DataFrame()
    for json_path in json_paths:
        with open(json_path) as json_file:
            json_data = json.load(json_file)
        
        data = json_data['annotations']
        
        df_people = pd.DataFrame(data)
        
        # filter only where the category id is 1
        df_people = df_people[df_people['category_id'] == 1]
        # now group by image id and get the count
        df_people = df_people[['image_id', 'id']].groupby('image_id').count()
        # define a new column 'label' and set it to 1
        df_people['label'] = 1
        # drop the column 'id'
        df_people = df_people.drop(['id'], axis=1)
        # alter the id column to 'file_name'
        df_people['file_name'] = df_people.index.astype(str) + '.png'
        # reset the index
        df_people = df_people.reset_index(drop=True)
        # add to the df_all
        df_all = pd.concat([df_all, df_people])
        
    # get all the images
    list_imgs = os.listdir('data/train')
    
    # create a dataframe
    df_imgs = pd.DataFrame(list_imgs)
    # rename the column
    df_imgs = df_imgs.rename(columns={0: 'file_name'})
    # create a new column 'label' and set it to 0
    df_imgs['label'] = 0
    
    # merge the two dataframes and sum the column label
    df = pd.concat([df_all, df_imgs]).groupby('file_name').sum()
    df = df.reset_index() 
    
    # save the dataframe to csv
    df.to_csv(csv_path, index=False)
        
    return df

json_paths = [
    'data/instances_train.json',
    'data/instances_val.json'
]

json_annotations_to_csv(json_paths, 'data/train.csv')