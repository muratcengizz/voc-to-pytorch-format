import xml.etree.ElementTree as ET
import os

def convert_voc_to_txt(xml_path, txt_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    with open(txt_path, 'w') as f:
        for object_elem in root.findall('object'):
            class_name = object_elem.find('name').text
            xmin = int(object_elem.find('bndbox/xmin').text)
            ymin = int(object_elem.find('bndbox/ymin').text)
            xmax = int(object_elem.find('bndbox/xmax').text)
            ymax = int(object_elem.find('bndbox/ymax').text)
            
            line = f'{class_name} {xmin} {ymin} {xmax} {ymax}\n'
            f.write(line)


path = os.chdir("C:/Users/murat/Documents/computer_vision3/mask_detection/valid/annotations")
path = os.listdir(path)
for element in path:
    xml_path = f'{element}'
    txt_path = f'{element[:-3]}.txt'
    convert_voc_to_txt(xml_path, txt_path)