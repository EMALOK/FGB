import json
from unittest import removeResult

def build(abs_file_path,out_path):

    file = open(abs_file_path,"r")

    json_file_content = file.read()

    file.close()

    style_dict_list = json.loads(json_file_content)

    print("list:",style_dict_list)

    for style_dict in style_dict_list:

        print("dict:",style_dict)

        inner_data = ""

        for key,value in style_dict.items():
            
            print(type(value))

            if type(value) is str:

                inner_data += f"{key} = \"{value}\","

            if type(value) is int:

                inner_data += f"{key} = {value},"

            if type(value) is bool:

                x = "true" if value else "false"

                inner_data += f"{key} = {x},"

        inner_data = inner_data[:-1]

        result = f"styles[\"{style_dict['name']}\"] = {{{inner_data}}}"


        print(result)