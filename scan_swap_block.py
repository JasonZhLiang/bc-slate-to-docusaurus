import json
import os
import re
import shutil

section = "2_capi"

source_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/{section}"

target_path = section

if not os.path.isdir(target_path):
    os.mkdir(target_path)

files_folders = os.scandir(source_path)
if section == '1_wrapper':
    for api_file in files_folders:
        if 'index.md' in api_file.name:
            shutil.copy(api_file, target_path)
        elif '.DS_Store' in api_file.name:
            print('skip .DS_Store file')
        else:
            with open(api_file, 'r') as source_api_file:
                content = source_api_file.read()
                api_definition = re.search(r'(?s)(.+?)## Usage', content).group(0)
                api_definition = re.sub(r'## Usage', '', api_definition)
                method_params = re.search(r'(?s)## Method Parameters(.+?)\n\n', content)
                # for those file with Method Parameters
                if method_params:
                    method_params = method_params.group(0)
                    usage_until_params = re.search(r'(?s)## Usage(.+?)## Method Parameters', content).group(0)
                    usage_until_params = re.sub(r'## Method Parameters', '', usage_until_params)
                    with open(f"{target_path}/{api_file.name}", "w+") as api_method:
                        api_method.write(f'{api_definition}')
                        api_method.write(f'{method_params}')
                        api_method.write(f'{usage_until_params}')
                else:
                    shutil.copy(api_file, target_path)
else:
    for item in files_folders:
        if os.path.isdir(item):
            service_dir_name = item.name
            service_path = os.path.join(target_path, item.name)
            source_service_path = os.path.join(source_path, item.name)
            os.mkdir(service_path)
            api_file_name_array = os.listdir(item)
            api_file_name_array.sort()
            for api_file in api_file_name_array:
                api_file_path = os.path.join(source_service_path, api_file)
                if 'index.md' in api_file:
                    shutil.copy(api_file_path, service_path)
                elif '.DS_Store' in api_file:
                    print('skip .DS_Store file')
                else:
                    with open(api_file_path, 'r') as source_api_file:
                        content = source_api_file.read()
                        api_definition = re.search(r'(?s)(.+?)## Usage', content).group(0)
                        api_definition = re.sub(r'## Usage', '', api_definition)
                        method_params = re.search(r'(?s)## Method Parameters(.+?)\n\n', content)
                        # for those file with Method Parameters
                        if method_params:
                            method_params = method_params.group(0)
                            usage_until_params = re.search(r'(?s)## Usage(.+?)## Method Parameters', content).group(0)
                            usage_until_params = re.sub(r'## Method Parameters', '', usage_until_params)
                            with open(f"{target_path}/{service_dir_name}/{api_file}", "w+") as api_method:
                                api_method.write(f'{api_definition}')
                                api_method.write(f'{method_params}')
                                api_method.write(f'{usage_until_params}')
                        else:
                            shutil.copy(api_file_path, service_path)
        else:
            shutil.copy(item, target_path)
