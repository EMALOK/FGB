import xml.etree.ElementTree as ET
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

    ok = True

    for i in root.iter():
        #utils.expl(i)
        if i.tag not in valid_types:
            ok = False
            utils.perr("parsed element not valid. element:",i)

    return ok