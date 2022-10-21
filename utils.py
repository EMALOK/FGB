

log_explain = False

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

    #gui element type
    gui_element["type"] = node.tag

    gui_element["parent_name"] = parent_name

    #gui element name
    if "name" in node.attrib.keys():
        gui_element["name"] = node.attrib["name"]
    else:
        #if not assigned create a name
        gui_element["name"] = f"unnamed_{unnamed_element_counter}"
        unnamed_element_counter += 1

    #gui element caption
    if "caption" in node.attrib.keys():
        gui_element["caption"] = node.attrib["caption"]

    
    #gui element tooltip
    if "tooltip" in node.attrib.keys():
        gui_element["tooltip"] = node.attrib["tooltip"]

    #gui element style
    if "style" in node.attrib.keys():
        gui_element["style"] = node.attrib["style"]

    #gui element style
    if "direction" in node.attrib.keys() and node.tag in ["frame","flow","line"]:
        gui_element["direction"] = node.attrib["direction"]

    return gui_element
