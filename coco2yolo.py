# this script is used to convert coco dataset to yolo dataset

# dependencies
import os
import json
import shutil

# # coco dataset path
# imgs_coco_path = './data/compressed_coco/images/val'
anns_coco_path = './data/compressed_coco/annotations/instances_val.json'
# # yolo dataset path
# imgs_yolo_path = './data/compressed_yolov8/val/images'
# anns_yolo_path = './data/compressed_yolov8/val/labels'

# # create yolo dataset path
# if not os.path.exists(imgs_yolo_path):
#     os.makedirs(imgs_yolo_path)
# if not os.path.exists(anns_yolo_path):
#     os.makedirs(anns_yolo_path)
    
# # copy images
# for img in os.listdir(os.path.join(imgs_coco_path)):
#         shutil.copy(os.path.join(imgs_coco_path, img), os.path.join(imgs_yolo_path, img))

# convert annotations
json = json.load(open(anns_coco_path))
# for imgs in json['images']:
#     width = imgs['width']
#     height = imgs['height']
#     image_id = imgs['id']
#     image_anns = []
    
#     for anns in json['annotations']:
#         if anns['image_id'] == image_id:
#             category_id = anns['category_id']
#             bbox = anns['bbox']
#             x = bbox[0]
#             y = bbox[1]
#             w = bbox[2]
#             h = bbox[3]
#             x_center = x + w / 2
#             y_center = y + h / 2
#             x_center /= width
#             y_center /= height
#             w /= width
#             h /= height
#             image_anns.append([category_id, x_center, y_center, w, h])
    
#     # save to a .txt file in yolo format
#     with open(os.path.join(anns_yolo_path, str(image_id) + '.txt'), 'w') as f:
#         for ann in image_anns:
#             f.write(' '.join(str(a) for a in ann) + '\n')
            
#     # print progress
#     print('Saving annotations for image: {}'.format(image_id))

print(json['categories'])