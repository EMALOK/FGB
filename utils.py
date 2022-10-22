

log_explain = False
unnamed_element_counter = 0

def expl(*parg):
    if log_explain:
        print(*parg)

def perr(*parg):
    print('\033[91m', *parg,'\033[0m')
    
def pwarn(*parg):
    print('\033[93m', *parg,'\033[0m')

def get_gui_element(parent_name,node):
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

    #gui element caption
    if "caption" in node.attrib.keys():
        gui_element["attrib"]["caption"] = node.attrib["caption"]

    
    #gui element tooltip
    if "tooltip" in node.attrib.keys():
        gui_element["attrib"]["tooltip"] = node.attrib["tooltip"]

    #gui element style
    if "style" in node.attrib.keys():
        gui_element["attrib"]["style"] = node.attrib["style"]

    #gui element style
    if "direction" in node.attrib.keys() and node.tag in ["frame","flow","line"]:
        gui_element["attrib"]["direction"] = node.attrib["direction"]

    return gui_element
