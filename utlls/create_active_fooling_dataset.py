import cv2
import os
import random
import numpy as np


folder = "../data/ILSVRC2012/targeted_dataset/"

class_1 = 673
class_2 = 281

class_1_folder = folder + str(class_1) + "/"
class_2_folder = folder + str(class_2) + "/"

dest_folder = (
    "../data/ILSVRC2012/targeted_dataset/"
    + str(min(class_1, class_2))
    + "_"
    + str(max(class_1, class_2))
    + "/"
)
if not os.path.exists: 
    os.mkdir(dest_folder)


def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


id = 0
for img_name in os.listdir(class_1_folder):
    img = cv2.imread(class_1_folder+img_name)
    img = cv2.resize(img, (112,112))
    
    # combine with random image from other class
    img2_name = random.choice(os.listdir(class_2_folder))
    img2 = cv2.imread(class_2_folder+img2_name)
    img2 = cv2.resize(img2, (112,112))
    
    print(type(img2))
    
    new_img = concat_tile([[img, img2], [img2, img]])
    print(dest_folder+str(id))
    cv2.imwrite(dest_folder+str(id)+".JPEG", new_img)
    id += 1
    

# TODO how to assign labels?
