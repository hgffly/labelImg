import os
import json
import codecs

JSON_EXT = '.json'
ENCODE_METHOD = 'utf-8'

class JsonWriter:

    #def __init__(self, foldername, filename, imgSize, databaseSrc='Unknown', localImgPath=None):
    def __init__(self, filename, imgSize):
        #self.foldername = foldername
        self.filename = filename  # image name
        #self.databaseSrc = databaseSrc
        self.imgSize = imgSize
        self.boxlist = []
        #self.localImgPath = localImgPath
        #self.verified = False

    def addBndBox(self, xmin, ymin, xmax, ymax, name, difficult):
        bndbox = {'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax}
        bndbox['name'] = name
        #bndbox['difficult'] = difficult
        self.boxlist.append(bndbox)

    def save(self, file_path):
        with open(file_path, "w") as f:
            json_obj = {"filename": self.filename, "height": self.imgSize[0], "width": self.imgSize[1], "depth": self.imgSize[2], "objs": self.boxlist}
            json.dump(json_obj, f)
