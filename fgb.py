import argparse
import os
import xml.etree.ElementTree as ET
import validate
import utils
import pprint

parser = argparse.ArgumentParser(description="Generate Factorio Guis")
parser.add_argument("in_file",nargs=1)
parser.add_argument("out_file",nargs=1)
parser.add_argument("--explain",action="store_true")

args = parser.parse_args()

#explain log flag
utils.log_explain = args.explain

in_file_path = os.path.abspath(args.in_file[0])
out_file_path = os.path.abspath(args.out_file[0])

utils.expl("in file:",in_file_path)
utils.expl("out file:",out_file_path)

tree = ET.parse(in_file_path)
root = tree.getroot()
parent_map = {c:p for p in tree.iter() for c in p}

if root.tag != "frame":
    utils.perr("the root element of file:",in_file_path,"isn't frame.","'",root.tag,"'","was detected")

if not validate.check_tree_types(root):
    quit(-1)

unnamed_element_counter = 0

gui_element_list = []

def iter(parent_name,node):

    gui_element = utils.get_gui_element(parent_name,node)

    gui_element_list.append(gui_element)

    for child in node:

        iter(gui_element["attrib"]["name"],child)

iter("",root)

for el in gui_element_list:

    inner_string = ""

    for key,value in el["attrib"].items():
        inner_string += f"{key}=\"{value}\","

    inner_string = inner_string[:-1]

    print(f'local {el["attrib"]["name"]} = {el["parent_name"]}.add{{{inner_string}}}')