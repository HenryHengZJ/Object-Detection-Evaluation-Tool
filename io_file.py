# coding=utf-8
import xml.dom.minidom

train_dir = "/mydrive/ObjDetection/Train"
classfile = "classes.txt"
class_map = {}

# Reading classes text file
with open(train_dir + '/' + classfile) as classiostream:
    classcontent = classiostream.read()

    for classline in classcontent.split("\n"):
        if classline != "":
            class_map[classline] = classline
            
def parse_xml(xml_path):
    dom = xml.dom.minidom.parse(xml_path)
    root = dom.documentElement
    objects = root.getElementsByTagName('object')
    gts = []
    for index, obj in enumerate(objects):
        name = obj.getElementsByTagName('name')[0].firstChild.data.decode('utf8')
        label = class_map[name]
        bndbox = obj.getElementsByTagName('bndbox')[0]
        x1 = int(bndbox.getElementsByTagName('xmin')[0].firstChild.data)
        y1 = int(bndbox.getElementsByTagName('ymin')[0].firstChild.data)
        x2 = int(bndbox.getElementsByTagName('xmax')[0].firstChild.data)
        y2 = int(bndbox.getElementsByTagName('ymax')[0].firstChild.data)
        gt_one = [label, x1, y1, x2, y2]
        gts.append(gt_one)
    return gts
