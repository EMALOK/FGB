import argparse
import os
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description="Generate Factorio Guis")
parser.add_argument("in_file",nargs=1)
parser.add_argument("out_file",nargs=1)
parser.add_argument("--explain",action="store_true")

args = parser.parse_args()

def expl(*parg):
    if args.explain:
        print(*parg)

def perr(*parg):
    print('\033[91m', *parg,'\033[0m')

in_file_path = os.path.abspath(args.in_file[0])
out_file_path = os.path.abspath(args.out_file[0])

expl("in file:",in_file_path)
expl("out file:",out_file_path)

tree = ET.parse(in_file_path)
root = tree.getroot()

if root.tag != "frame":
    perr("the root element of file:",in_file_path,"isn't frame.","'",root.tag,"'","was detected")