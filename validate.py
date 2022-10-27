import xml.etree.ElementTree as ET
import builder.component as component
import utils

valid_types = [
    "button",
    "sprite-button",
    "checkbox",
    "flow",
    "frame",
    "label",
    "line",
    "progressbar",
    "table",
    "textfield",
    "radiobutton",
    "sprite",
    "scroll-pane",
    "drop-down",
    "list-box",
    "camera",
    "choose-elem-button",
    "text-box",
    "slider",
    "minimap",
    "entity-preview",
    "empty-widget",
    "tabbed-pane",
    "tab",
    "switch"
]

def check_tree_types(root: ET.Element):
    for i in list(root.iter()):
        #utils.expl(i)
        if i.tag not in valid_types:

            comp = component.translate_component(i)
            i.tag = comp.tag
            i.attrib = comp.attrib

            print(i)

    print(list(root.iter()))