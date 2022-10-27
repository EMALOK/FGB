import os
import xml.etree.ElementTree as ET
import glob

from utils import perr


component_folder = ""

def translate_component(node:ET.Element):

    file = component_folder+"/"+node.tag+".component.xml"

    if os.path.exists(file):

        tree = ET.parse(file)

        root = tree.getroot()

        component = root[0]

        print(component)

        return component
    else:
        perr("component:",file,"not found")
        quit(-1)
