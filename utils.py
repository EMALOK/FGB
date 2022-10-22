

from xml.etree.ElementTree import Element


log_explain = False
unnamed_element_counter = 0

def expl(*parg):
    if log_explain:
        print(*parg)

def perr(*parg):
    print('\033[91m', *parg,'\033[0m')
    
def pwarn(*parg):
    print('\033[93m', *parg,'\033[0m')

def get_gui_element(parent_name,node:Element):
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


        gui_element["attrib"][key] = node.attrib[key]

    return gui_element
