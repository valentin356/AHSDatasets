import cv2
import os
import json
import copy
import numpy as np

#custom image filters for preprocess
def delImg(directory):
    if ("ann.json" in os.listdir(directory)):
        with open(directory+'ann.json') as json_file: 
            data = json.load(json_file)
        nData = copy.deepcopy(data)
        nJsonsv = ""
        svJson = ""
        x = 0
        names = []
        nameID = []
        for filename in os.listdir(directory):
            if (filename[-4:]=='.png') and (filename in nData):
                names.append(filename)
            else:
                os.remove(directory+filename)
delImg("C:/Users/Valentin/Desktop/Kurzusokhoz/efop_sajat/datasets/train/")