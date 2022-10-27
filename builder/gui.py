import copy
import os
import pprint
from typing import List
import xml.etree.ElementTree as ET
import validate
import utils
import template.gui_template as gui_template
import template.event_template as event_template


unnamed_element_counter = 0

component_folder = ""

#removed on_gui_opened and on_gui_closed
#example:
#"on_gui_click":[
#   {
#       name:"button_1",
#       body:"code here or expose"
#   }
# ]
gui_events = {
    "on_gui_checked_state_changed":[],
    "on_gui_click":[],
    "on_gui_confirmed":[],
    "on_gui_elem_changed":[],
    "on_gui_location_changed":[],
    "on_gui_selected_tab_changed":[],
    "on_gui_selection_state_changed":[],
    "on_gui_switch_state_changed":[],
    "on_gui_text_changed":[],
    "on_gui_value_changed":[]
}

def get_gui_element(parent_name,node:ET.Element):
    global unnamed_element_counter

    gui_element = {}

    gui_element["attrib"] = {}

    #gui element type
    gui_element["attrib"]["type"] = node.tag

    gui_element["parent_name"] = parent_name

    #gui element name
    if "name" in node.attrib.keys():
        gui_element["attrib"]["name"] = node.attrib["name"].replace("-","_")
    else:
        #if not assigned create a name
        gui_element["attrib"]["name"] = f"unnamed_{unnamed_element_counter}"
        unnamed_element_counter += 1

    #those without excetion are translated directlsy

    for key,value in node.attrib.items():

        if key == "direction" and node.tag not in ["frame","flow","line"]:
            continue

        if key == "on_click" and node.tag in ["button","sprite-button"]:
            #add the event to the list and don't add it to the  attrib
            gui_events["on_gui_click"].append({
                "name":gui_element["attrib"]["name"],
                "body":value
            })
            continue

        gui_element["attrib"][key] = node.attrib[key]

    return gui_element


def iter(parent_name,node):

    res = []

    gui_element = get_gui_element(parent_name,node)

    res.append(gui_element)

    for child in node:

        res = res + iter(gui_element["attrib"]["name"],child)

    return res


def build(abs_file_path,out_path) :
    
    #get the xml tree
    tree = ET.parse(abs_file_path)

    #<gui> root
    root = tree.getroot()

    #check the correct root
    if root.tag != "gui":
        utils.perr("the root element of file:",abs_file_path,"isn't gui.","'",root.tag,"'","was detected")
        return -1


    gui_root = root[0]
    validate.check_tree_types(gui_root)

    extra_code = ""

    #extra code todo actual detection
    if len(root) == 2:
        extra_code = root[1].text

    gui_element_list = iter("root",gui_root)

    #pprint.pprint(gui_element_list)

    gui_build = ""

    for el in gui_element_list:

        inner_string = ""


        for key,value in el["attrib"].items():

            if value == "true" or value == "false":
                inner_string += f"{key}={value},"
                continue


            if key == "lcaption":
                inner_string += f"caption={{\"{value}\"}},"
                continue

            inner_string += f"{key}=\"{value}\","

        inner_string = inner_string[:-1]

        gui_build += f'local {el["attrib"]["name"]} = {el["parent_name"]}.add{{{inner_string}}}\n'


    bind_events = ""

    #bind events
    for event_type in gui_events:

        curr_event = copy.deepcopy(event_template.event_template)
        curr_event = curr_event.replace(r"{%event_name%}",event_type)

        event_element_body = ""

        for event_type_element_bind in gui_events[event_type]:

            event_element_body += copy.deepcopy(event_template.event_element_template)
            event_element_body = event_element_body.replace(r"{%element_name%}",event_type_element_bind["name"])
            event_element_body = event_element_body.replace(r"{%event_element_body%}",event_type_element_bind["body"])


        curr_event = curr_event.replace(r"{%event_body%}",event_element_body)
        bind_events += curr_event

    #generate the .lua file
    template = copy.deepcopy(gui_template.gui_template)

    #close gui name reference
    template = template.replace(r"{%gui_name%}",gui_element_list[0]["attrib"]["name"])

    #gui_build
    template = template.replace(r"{%gui_build%}",gui_build)

    #extra_code
    template = template.replace(r"{%extra_code%}",extra_code)
    
    #todo events
    template = template.replace(r"{%bind_events%}",bind_events)
    
    
    gui_folder = out_path + "/gui"

    file_name = os.path.splitext(os.path.basename(abs_file_path))[0].replace(".","_")

    #folder exist
    if not os.path.isdir(gui_folder):
        os.mkdir(gui_folder)

    file_out = open(gui_folder + "/" + file_name + ".lua","w")

    file_out.write(template)

    file_out.close()


