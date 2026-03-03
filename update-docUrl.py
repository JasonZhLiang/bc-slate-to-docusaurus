import re
import os


# find and replace https://getbraincloud.com/apidocs/apiref/#capi-appstore-verifypurchase
# to https://docs.braincloudservers.com/api/capi/appstore/verifypurchase

def json_file_docurl_process(content, sanitize_folder):
    current_link = re.search(r'(?s)/#(.+?)"', content)
    files = os.scandir(sanitize_folder)
    exist_s2s_method_name_array = [file.name.split('.')[0] for file in files if ".md" in file.name]
    # print(exist_s2s_method_name_array)
    while current_link:
        link_url_value = current_link.group(1).strip()
        link_url_value_alter = re.sub(r'-', '/', link_url_value)
        exist_s2s_method_name = link_url_value_alter.split('/')[-1]
        # print(exist_s2s_method_name)
        if exist_s2s_method_name not in exist_s2s_method_name_array:
            # print(exist_s2s_method_name)
            link_url_value_alter = re.sub(f'{exist_s2s_method_name}', '', link_url_value_alter)
            # print(link_url_value_alter)
        content = re.sub(r'(?s)/#(.+?)"', f'/{link_url_value_alter}"', content, 1)
        current_link = re.search(r'(?s)/#(.+?)"', content)

    content = re.sub(r'https://getbraincloud.com/apidocs/apiref', 'https://docs.braincloudservers.com/api', content)
    return content


# now we are using new docUrls "https://docs.braincloudservers.com/api/s2s/customentity/sysdropcollection",
# but for s2s, we don't have that file in s2s customentity folder, so we need to
# change it to the parent folder "https://docs.braincloudservers.com/api/s2s/customentity/"
def sanitize_json_file_docurl_process(content, sanitize_folder):
    current_link = re.search(r'(?s)http://docs(.+?)"', content)
    files = os.scandir(sanitize_folder)
    exist_s2s_method_name_array = [file.name.split('.')[0] for file in files if ".md" in file.name]
    while current_link:
        link_url_value = current_link.group(1).strip()
        exist_s2s_method_name = link_url_value.split('/')[-1]
        link_url_value_alter = link_url_value
        if exist_s2s_method_name not in exist_s2s_method_name_array:
            # print(exist_s2s_method_name)
            link_url_value_alter = re.sub(f'/{exist_s2s_method_name}', '', link_url_value)

            print(link_url_value)
            print(link_url_value_alter)
            content = re.sub(rf'{link_url_value}', f'{link_url_value_alter}', content, 1)
        content = re.sub(r'http://docs', f'https://docs', content, 1)
        current_link = re.search(r'(?s)http://docs(.+?)"', content)

    return content


source_path = f"/Users/jasonl/bitbucket/braincloud-portal/Development/Server-AppServer/src/main/webapp/js/s2sJson/"

target_path = f"s2sjson-folder"

# for s2sJson only
sanitize_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/4_s2s/"

if not os.path.isdir(target_path):
    os.mkdir(target_path)

files = os.scandir(source_path)

json_file_name_array = [file.name for file in files if ".json" in file.name]
json_file_name_array.sort()
# print(json_file_name_array)
for json_file in json_file_name_array:
    json_file_path = os.path.join(source_path, json_file)
    # comparing with bcdocs s2s methods
    if json_file == "Authenticate.json":
        json_file = "authentication.json"
    elif json_file == "GlobalFileV3.json":
        json_file = "GlobalFile.json"
    elif json_file == "RTTRegistration.json":
        json_file = "rtt.json"
    elif json_file == "ScriptService.json":
        json_file = "Script.json"
    elif json_file == "GlobalGameStatistics.json":
        json_file = "GlobalStats.json"
    sanitize_folder = os.path.join(sanitize_path, json_file.lower().split('.json')[0])
    with open(json_file_path, 'r') as source_api_file:
        content = source_api_file.read()
        content = json_file_docurl_process(content, sanitize_folder)
        content = re.sub(r'https://docs', f'http://docs', content)
        content = sanitize_json_file_docurl_process(content, sanitize_folder)
    with open(f"{target_path}/{json_file}", "w+") as new_json_file:
        new_json_file.write(f'{content.strip()}')

# test string split to get the last part of "https://docs.braincloudservers.com/api/capi/appstore/verifypurchase",
# i.e. "verifypurchase" or using re.search

# s = "https://docs.braincloudservers.com/api/capi/appstore/verifypurchase"
# m = re.search(r'(?<=\/)[^.]*$', s)
# print(m.relay())
# phase = s.split('/')[-1]
# print(phase)
