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


class JsonReader:
    def __init__(self, filepath):
        # shapes type:
        # [labbel, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], color, color, difficult]
        self.shapes = []
        self.filepath = filepath

        with open(filepath, "r") as f:
            obj = json.load(f)

        self.imgSize = [obj["height"], obj["width"], obj["depth"]]

        self.parseJsonFormat(obj)

    def getShapes(self):
        return self.shapes

    def addShape(self, label, xmin, ymin, xmax, ymax, difficult):
        points = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
        self.shapes.append((label, points, None, None, difficult))

    def parseJsonFormat(self, obj):
        #bndBoxFile = open(self.filepath, 'r')
        for bb in obj["objs"]:
            #classIndex, xcen, ycen, w, h = bndBox.split(' ')
            label, xmin, ymin, xmax, ymax = bb["name"], bb["xmin"], bb["ymin"], bb["xmax"], bb["ymax"]  #self.yoloLine2Shape(classIndex, xcen, ycen, w, h)

            # Caveat: difficult flag is discarded when saved as yolo format.
            self.addShape(label, xmin, ymin, xmax, ymax, False)
