import re
import os

# change the section name here (capi, s2s, cc, appendix, wrapper)
section = 'capi'

csharp_head = """
```mdx-code-block
<BrowserWindow>
<Tabs>
<TabItem value="csharp" label="C#">
```
"""
cpp_head = """
```mdx-code-block
</TabItem>
<TabItem value="cpp" label="C++">
```
"""
objective_c_head = """
```mdx-code-block
</TabItem>
<TabItem value="objectivec" label="Objective-C">
```
"""
java_head = """
```mdx-code-block
</TabItem>
<TabItem value="java" label="Java">
```
"""
javascript_head = """
```mdx-code-block
</TabItem>
<TabItem value="js" label="JavaScript">
```
"""
cfs_head = """
```mdx-code-block
</TabItem>
<TabItem value="cfs" label="Cloud Code">
```
"""
r_head = """
```mdx-code-block
</TabItem>
<TabItem value="r" label="Raw">
```
"""
block_end = """
```mdx-code-block
</TabItem>
</Tabs>
</BrowserWindow>
```
"""


# replace aside note and keep origin class type as is
def replace_aside_note(content):
    content = re.sub(r'<aside\sclass="(.+?)">', r':::\1', content)
    content = re.sub(r'</aside>', ':::', content)
    return content


# replace notice and warning aside note to tip and caution
def replace_notice_warning_note(content):
    content = re.sub(r':::notice', ':::tip', content)
    content = re.sub(r':::warning', ':::caution', content)
    return content


# replace single backtick with triple one
def replace_single_backtick(content):
    content = re.sub(r'\n`\n', r'\n```\n', content)
    return content


# take off jsonBtn
def take_jsonbtn(content):
    content = re.sub(r'<%= partial "partials/jsonBtn" %>', r'', content)
    return content


# replace img link
def img_link_process(content):
    content = re.sub(r'<%= I18n\.t\(:root\) %> <%= data\.images\.(.+?)\s%>', r'@site/docs/img/api-img/\1.png', content)
    return content


# store code block then remove it from origin
code_block_value = ''


def code_block_process(block_name, content):
    code_block = re.search(f'(?s)```{block_name}(.+?)```', content)
    global code_block_value
    if code_block:
        code_block_value = code_block.group(0)
        if block_name == "json-doc":
            code_block_value = re.sub(f'{block_name}', r'json', code_block_value)
        elif block_name == "objective_c":
            code_block_value = re.sub(f'{block_name}', r'objectivec', code_block_value)
        content = re.sub(f'(?s)```{block_name}(.+?)```', r'', content, 1)
    return {"code_block": code_block_value, "content": content}


# json_doc_block = code_block_process("json-doc", context)['code_block']
# context = code_block_process("json-doc", context)['content']
# context = code_block_process("objective_c", context)['content']


# extract partials/servop
service_name_value = ''
operation_name_value = ''


def serv_op_process(content):
    serv_op = re.search(r'(?s)<%= partial\(:"partials/servop"(.+?)%>', content)
    global service_name_value
    global operation_name_value
    if serv_op:
        service_name = re.search(r'(?s):service_name => "(.+?)"', serv_op.group(0))
        service_name_value = service_name.group(1)
        operation_name = re.search(r'(?s):operation_name => "(.+?)"', serv_op.group(0))
        operation_name_value = operation_name.group(1)
        content = re.sub(r'(?s)<%= partial\(:"partials/servop"(.+?)%>', r'', content)
    return {"service_name": service_name_value, "operation_name": operation_name_value, "content": content}


# context = serv_op_process(context)['content']

# get rid of version partial
def take_version_tag(content):
    content = re.sub(r'(?s)<%= partial\(:"partials/versionTag"(.+?)%>', r'', content)
    return content


# get rid of version partial
def take_doc_example_tag(content):
    content = re.sub(r'(?s)<%= partial\(:"partials/docExample"(.+?)%>', r'', content)
    return content


# get rid of errorHandlingBtn partial
def replace_error_handling(content):
    content = re.sub(r'(?s)<%= partial\s"partials/errorHandlingBtn"(.+?)%>', r'### Error Handling Example', content)
    return content


# replace title to take off [] if it has any
title_text_alter = ''


def title_process(content):
    title_text = re.search(r'^##?\s(.+?)\[.+\]', content)
    global title_text_alter
    if title_text:
        title_text_alter = re.sub(r'\[.+\]', '', title_text.group(0)).strip()
        title_text_alter = re.sub(r'##?', '', title_text_alter).strip()
        content = re.sub(r'^##?\s(.+?)\[.+\]', '\n', content)
    return {"title": title_text_alter, "content": content}


api_title_text_alter = ''


def api_title_process(content):
    title_text = re.search(r'^###\s(.+?)\n', content)
    global api_title_text_alter
    if title_text:
        api_title_text_alter = re.sub(r'###', '', title_text.group(0)).strip()
        api_title_text_alter = re.sub(r'\[.+\]', '', api_title_text_alter).strip()
        content = re.sub(r'^###\s(.+?)\n', '\n', content)
    return {"title": api_title_text_alter, "content": content}


def appendix_title_process(content):
    title_text = re.search(r'^##\s(.+?)\n', content)
    global api_title_text_alter
    if title_text:
        api_title_text_alter = re.sub(r'##', '', title_text.group(0)).strip()
        api_title_text_alter = re.sub(r'\[.+\]', '', api_title_text_alter).strip()
        content = re.sub(r'^##\s(.+?)\n', '\n', content)
    return {"title": api_title_text_alter, "content": content}


# select method parameters block
# in case some files don't have a blank line at the end of method parameters block, add one here
param_block_value = ''


def param_block_process(content):
    content = content + "\n\n"
    global param_block_value
    param_block = re.search(r'(?s)## Method Parameters(.+?)\n\n', content)
    if param_block:
        param_block_value = param_block.group(0)
        content = re.sub(r'(?s)#### Method(.+?)\n\n', '', content)
    return {"param_block": param_block_value, "content": content}


# context = param_block_process(context)['content']

# set all h4, h5 level up two to h3, h4 accordingly
def header_level_up_process(content):
    content = re.sub(r'###', r'##', content)
    return content


# find and replace anchor tag with internal file link
# e.g. <a href="#" onclick='window.navigateToTarget("#capi-authentication");'>Authentication</a>
# to [Authentication](/api/capi/authentication)
def anchor_process(content):
    current_anchor = re.search(r'(?s)<a href="#"(.+?)</a>', content)
    link_text_value = 'xxxx'
    link_url_value_alter = 'zzzz'
    while current_anchor:
        link_text_search = re.search(r"(?s);'>(.+?)</a>", current_anchor.group(0))
        if link_text_search:
            link_text_value = link_text_search.group(1).strip()
            link_url_search = re.search(r'(?s)\("#(.+?)"\)', current_anchor.group(0))
            link_url_value = link_url_search.group(1).strip()
            link_url_value_alter = "/api/" + re.sub(r'-', '/', link_url_value)
        content = re.sub(r"(?s)<a(.+?)</a>", f'[{link_text_value}]({link_url_value_alter})', content, 1)
        current_anchor = re.search(r"(?s)<a(.+?)</a>", content)
    return content


# context = anchor_process(context)

# find and replace md standard internal file link from [SysCreateEntity](#capi-customentity-syscreateentity)
# to [SysCreateEntity](/api/capi/customentity/syscreateentity)
def internal_file_link_process(content):
    current_link = re.search(r'(?s)\(#(.+?)\)', content)
    while current_link:
        link_url_value = current_link.group(1).strip()
        link_url_value_alter = "/api/" + re.sub(r'-', '/', link_url_value)
        content = re.sub(r'(?s)\(#(.+?)\)', f'({link_url_value_alter})', content, 1)
        current_link = re.search(r'(?s)\(#(.+?)\)', content)
    return content


# reset global values
def reset_global_values():
    global param_block_value, service_name_value, operation_name_value, code_block_value
    param_block_value = ''
    service_name_value = ''
    operation_name_value = ''
    code_block_value = ''


# context = internal_file_link_process(context)



source_path = f"/Users/jasonl/bitbucket/braincloud-apiref/source/localizable/en/includes/{section}"
# if not os.path.isdir("target_folder"):
#     os.mkdir("target_folder")

if section == "wrapper":
    target_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/1_{section}"
if section == "capi":
    target_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/2_{section}"
if section == "cc":
    target_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/3_{section}"
if section == "s2s":
    target_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/4_{section}"
if section == "appendix":
    target_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/5_{section}"

if not os.path.isdir(target_path):
    os.mkdir(target_path)

files = os.scandir(source_path)
print(files)

if section == 'wrapper' or section == 'appendix':
    section_file_name_array = [file.name for file in files]
    section_file_name_array.sort()
    content_index = ''
    title_index = ''
    for api_file in section_file_name_array:
        api_file_path = os.path.join(source_path, api_file)
        if '__' in api_file:
            with open(api_file_path, 'r') as source_api_file:
                content = source_api_file.read()
                processed_data = title_process(content)
                title_index = processed_data['title']
                content = processed_data['content']
                content = replace_aside_note(content)
                content = replace_notice_warning_note(content)
                content = replace_error_handling(content)
                content = anchor_process(content)
                content = internal_file_link_process(content)
                content = img_link_process(content)
                content = header_level_up_process(content)
                content = take_jsonbtn(content)
                content = take_version_tag(content)
                content = take_doc_example_tag(content)
                content = replace_single_backtick(content)
                content_index = content_index + content + '\n'
        else:
            api_file_name_updated = re.sub(r'_(.+?)_', r'', api_file)
            api_file_name_updated = re.sub(r'\.erb', r'', api_file_name_updated)
            with open(api_file_path, 'r') as source_api_file:
                reset_global_values()
                content = source_api_file.read()
                if section == 'appendix':
                    processed_data = appendix_title_process(content)
                else:
                    processed_data = api_title_process(content)
                _title = processed_data['title']
                content = processed_data['content']
                content = replace_aside_note(content)
                content = replace_notice_warning_note(content)
                content = replace_error_handling(content)
                content = anchor_process(content)
                content = internal_file_link_process(content)
                content = img_link_process(content)
                content = take_jsonbtn(content)
                content = take_version_tag(content)
                content = take_doc_example_tag(content)
                content = replace_single_backtick(content)
                processed_data = param_block_process(content)
                _param_block = processed_data['param_block']
                content = processed_data['content']
                processed_data = serv_op_process(content)
                _service_name = processed_data['service_name']
                _operation_name = processed_data['operation_name']
                content = processed_data['content']
                processed_data = code_block_process("csharp", content)
                _csharp_block = processed_data['code_block']
                content = processed_data['content']
                processed_data = code_block_process("cpp", content)
                _cpp_block = processed_data['code_block']
                content = processed_data['content']
                processed_data = code_block_process("objective_c", content)
                _objective_c_block = processed_data['code_block']
                content = processed_data['content']
                processed_data = code_block_process("java", content)
                _java_block = processed_data['code_block']
                content = processed_data['content']
                processed_data = code_block_process("javascript", content)
                _javascript_block = processed_data['code_block']
                content = processed_data['content']
                processed_data = code_block_process("cfscript", content)
                _cfs_block = processed_data['code_block']
                content = processed_data['content']
                processed_data = code_block_process("r", content)
                _r_block = processed_data['code_block']
                content = processed_data['content']
                processed_data = code_block_process("json-doc", content)
                _json_doc_block = processed_data['code_block']
                content = processed_data['content']
                content = header_level_up_process(content)
            with open(f"{target_path}/{api_file_name_updated}", "w+") as api_method:
                api_method.write(f'# {_title}\n')
                api_method.write(f'## Overview\n')
                api_method.write(f'{content.strip()}\n\n')
                if _service_name:
                    api_method.write(
                        f'<PartialServop service_name="{_service_name}" operation_name="{_operation_name}" />\n\n')
                if _csharp_block or _cpp_block or _objective_c_block or _java_block or _javascript_block or _cfs_block or _r_block:
                    api_method.write(f'## Usage\n')
                    api_method.write(f'{csharp_head}\n')
                    api_method.write(f'{_csharp_block}\n')
                    api_method.write(f'{cpp_head}\n')
                    api_method.write(f'{_cpp_block}\n')
                    api_method.write(f'{objective_c_head}\n')
                    api_method.write(f'{_objective_c_block}\n')
                    api_method.write(f'{java_head}\n')
                    api_method.write(f'{_java_block}\n')
                    api_method.write(f'{javascript_head}\n')
                    api_method.write(f'{_javascript_block}\n')
                    api_method.write(f'{cfs_head}\n')
                    api_method.write(f'{_cfs_block}\n')
                    api_method.write(f'{r_head}\n')
                    api_method.write(f'{_r_block}\n')
                    api_method.write(f'{block_end}\n')
                if _json_doc_block:
                    api_method.write(f'<details>\n')
                    api_method.write(f'<summary>JSON Response</summary>\n\n')
                    api_method.write(f'{_json_doc_block}\n')
                    api_method.write(f'</details>\n')
                    api_method.write(f'\n')
                if _param_block:
                    api_method.write(f'{_param_block}\n')
                for line in api_method:
                    if line.strip():
                        api_method.write(line)

    with open(f"{target_path}/index.md", "w") as service_index:
        service_index.write(f'# {title_index}\n')
        service_index.write(f'## Overview\n')
        service_index.write(f'{content_index}\n')
        service_index.write(f'<DocCardList />')
# for capi, cc, s2s section
else:
    for file in files:
        if os.path.isdir(file):
            service_dir_name = file.name
            service_path = os.path.join(target_path, file.name)
            source_service_path = os.path.join(source_path, file.name)
            if os.path.isdir(service_path):
                print('delete target_folder and re-try')
                break
            os.mkdir(service_path)
            # api_file_array = os.scandir(source_service_path)
            # api_file_name_array = []
            # for api_file in api_file_array:
            #     api_file_name_array.append(api_file.name)

            api_file_name_array = os.listdir(file)
            api_file_name_array.sort()
            content_index = ''
            title_index = ''
            for api_file in api_file_name_array:
                api_file_path = os.path.join(source_service_path, api_file)
                if '__' in api_file:
                    with open(api_file_path, 'r') as source_api_file:
                        content = source_api_file.read()
                        processed_data = title_process(content)
                        title_index = processed_data['title']
                        content = processed_data['content']
                        content = replace_aside_note(content)
                        content = replace_notice_warning_note(content)
                        content = replace_error_handling(content)
                        content = anchor_process(content)
                        content = internal_file_link_process(content)
                        content = img_link_process(content)
                        content = header_level_up_process(content)
                        content = take_jsonbtn(content)
                        content = take_version_tag(content)
                        content = take_doc_example_tag(content)
                        content = replace_single_backtick(content)
                        content_index = content_index + content + '\n'
                else:
                    api_file_name_updated = re.sub(r'_(.+?)_', r'', api_file)
                    api_file_name_updated = re.sub(r'\.erb', r'', api_file_name_updated)
                    with open(api_file_path, 'r') as source_api_file:
                        reset_global_values()
                        content = source_api_file.read()
                        processed_data = api_title_process(content)
                        _title = processed_data['title']
                        content = processed_data['content']
                        content = replace_aside_note(content)
                        content = replace_notice_warning_note(content)
                        content = replace_error_handling(content)
                        content = anchor_process(content)
                        content = internal_file_link_process(content)
                        content = img_link_process(content)
                        content = take_jsonbtn(content)
                        content = take_version_tag(content)
                        content = take_doc_example_tag(content)
                        content = replace_single_backtick(content)
                        processed_data = param_block_process(content)
                        _param_block = processed_data['param_block']
                        content = processed_data['content']
                        processed_data = serv_op_process(content)
                        _service_name = processed_data['service_name']
                        _operation_name = processed_data['operation_name']
                        content = processed_data['content']
                        processed_data = code_block_process("json-doc", content)
                        _json_doc_block = processed_data['code_block']
                        content = processed_data['content']
                        processed_data = code_block_process("csharp", content)
                        _csharp_block = processed_data['code_block']
                        content = processed_data['content']
                        processed_data = code_block_process("cpp", content)
                        _cpp_block = processed_data['code_block']
                        content = processed_data['content']
                        processed_data = code_block_process("objective_c", content)
                        _objective_c_block = processed_data['code_block']
                        content = processed_data['content']
                        processed_data = code_block_process("java", content)
                        _java_block = processed_data['code_block']
                        content = processed_data['content']
                        processed_data = code_block_process("javascript", content)
                        _javascript_block = processed_data['code_block']
                        content = processed_data['content']
                        processed_data = code_block_process("cfscript", content)
                        _cfs_block = processed_data['code_block']
                        content = processed_data['content']
                        processed_data = code_block_process("r", content)
                        _r_block = processed_data['code_block']
                        content = processed_data['content']
                        content = header_level_up_process(content)
                    with open(f"{target_path}/{service_dir_name}/{api_file_name_updated}", "w+") as api_method:
                        api_method.write(f'# {_title}\n')
                        api_method.write(f'## Overview\n')
                        api_method.write(f'{content.strip()}\n\n')
                        if _service_name:
                            api_method.write(
                                f'<PartialServop service_name="{_service_name}" operation_name="{_operation_name}" />\n\n')
                        api_method.write(f'## Usage\n')
                        api_method.write(f'{csharp_head}\n')
                        api_method.write(f'{_csharp_block}\n')
                        api_method.write(f'{cpp_head}\n')
                        api_method.write(f'{_cpp_block}\n')
                        api_method.write(f'{objective_c_head}\n')
                        api_method.write(f'{_objective_c_block}\n')
                        api_method.write(f'{java_head}\n')
                        api_method.write(f'{_java_block}\n')
                        api_method.write(f'{javascript_head}\n')
                        api_method.write(f'{_javascript_block}\n')
                        api_method.write(f'{cfs_head}\n')
                        api_method.write(f'{_cfs_block}\n')
                        api_method.write(f'{r_head}\n')
                        api_method.write(f'{_r_block}\n')
                        api_method.write(f'{block_end}\n')
                        if _json_doc_block:
                            api_method.write(f'<details>\n')
                            api_method.write(f'<summary>JSON Response</summary>\n\n')
                            api_method.write(f'{_json_doc_block}\n')
                            api_method.write(f'</details>\n')
                            api_method.write(f'\n')
                        if _param_block:
                            api_method.write(f'{_param_block}\n')
                        for line in api_method:
                            if line.strip():
                                api_method.write(line)

            with open(f"{target_path}/{service_dir_name}/index.md", "w") as service_index:
                service_index.write(f'# {title_index}\n')
                service_index.write(f'## Overview\n')
                service_index.write(f'{content_index}\n')
                service_index.write(f'<DocCardList />')

        elif file.name != ".DS_Store":
            with open(file, "r") as source_file:
                content = source_file.read()
                processed_data = title_process(content)
                _title = processed_data['title']
                content = processed_data['content']
                content = replace_aside_note(content)
                content = replace_notice_warning_note(content)
                content = replace_error_handling(content)
                content = anchor_process(content)
                content = internal_file_link_process(content)
                content = img_link_process(content)
                content = header_level_up_process(content)
                content = take_jsonbtn(content)
                content = take_version_tag(content)
                content = take_doc_example_tag(content)
                content = replace_single_backtick(content)
            if "_.md" in file.name:
                with open(f"{target_path}/index.md", "a") as section_index:
                    section_index.write(f'# {_title}\n')
                    section_index.write(f'## Overview\n')
                    section_index.write(f'{content}\n')
                    section_index.write(f'<DocCardList />')
            else:
                with open(f"{target_path}/writingscript.md", "a") as section_index:
                    section_index.write(f'# {_title}\n')
                    section_index.write(f'## Overview\n')
                    section_index.write(f'{content}\n')
                    section_index.write(f'<DocCardList />')
