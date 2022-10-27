import argparse
import os
import glob
import time 

import builder.gui as gui
import builder.component as component

parser = argparse.ArgumentParser(description="Generate Factorio mods")
parser.add_argument("in_folder",nargs=1,help="the input folder to build")
parser.add_argument("out_folder",nargs=1,help="the output folder where to store the result")
parser.add_argument("--explain",action="store_true",help="verbose logging")

args = parser.parse_args()


input_file_paths = glob.glob(f"{os.path.abspath(args.in_folder[0])}/*")

component.component_folder = f"{os.path.abspath(args.in_folder[0])}/components"

#print(input_file_paths)


for file_path in input_file_paths:

    print(file_path)

    if "gui.xml" in file_path:

        gui.build(file_path,args.out_folder[0])