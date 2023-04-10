import re
import os
import time
import shutil


# replace some broken image links problem from
# [![](images/googleAuth_02.jpg)](/apidocs/wp-content/uploads/2016/10/googleAuth_02.jpg) to
# [![](images/googleAuth_02.jpg)](https://getbraincloud.com/apidocs/wp-content/uploads/2016/10/googleAuth_02.jpg) then
# [![](images/googleAuth_02.jpg)](images/googleAuth_02.jpg)
def image_link_add_https_process(content):
    content = re.sub(r'(?s)\(http://apidocs.braincloudservers.com/', r'(https://getbraincloud.com/apidocs/', content)
    content = re.sub(r'(?s)\(/apidocs/wp-content/', r'(https://getbraincloud.com/apidocs/wp-content/', content)
    content = re.sub(r'(?s)\(https://getbraincloud.com/apidocs/wp-content/uploads/\d{4}/\d{2}/', r'(images/', content)
    content = re.sub(r'(?s)\(https://staging.getbraincloud.com/apidocs/wp-content/uploads/\d{4}/\d{2}/', r'(images/', content)
    return content


# replace the wrong apiref links problem from
# (/apidocs/apiref/#capi-customentity) to (/api/capi/customeentity)
# [![](images/googleAuth_02.jpg)](https://getbraincloud.com/apidocs/wp-content/uploads/2016/10/googleAuth_02.jpg)
def apiref_link_process(content):
    content = re.sub(r'(?s)http://internal.braincloudservers.com/s3/apidocs/index.html', r'/apidocs/apiref/', content)
    content = re.sub(r'(?s)/apidocs/apiref/index.html', r'/apidocs/apiref/', content)
    content = re.sub(r'(?s)/apidocs/apiref/\?(.+?)#', r'/apidocs/apiref/#', content)
    content = re.sub(r'(?s)https://getbraincloud.com/apidocs/apiref/', r'/apidocs/apiref/', content)
    content = re.sub(r'(?s)https://staging.getbraincloud.com/apidocs/apiref/', r'/apidocs/apiref/', content)
    current_link = re.search(r'(?s)/apidocs/apiref/#(.+?)\)', content)
    while current_link:
        link_url_value = current_link.group(1).strip()
        link_url_value_alter = "/api/" + re.sub(r'-', '/', link_url_value)
        content = re.sub(r'(?s)/apidocs/apiref/#(.+?)\)', f'{link_url_value_alter})', content, 1)
        current_link = re.search(r'(?s)/apidocs/apiref/#(.+?)\)', content)
    # for cases like [BrainCloudClient.RegisterFileUploadCallback](/apiref/#capi-client-registerfileuploadcallback)
    current_link = re.search(r'(?s)\(/apiref/#(.+?)\)', content)
    while current_link:
        link_url_value = current_link.group(1).strip()
        link_url_value_alter = "/api/" + re.sub(r'-', '/', link_url_value)
        content = re.sub(r'(?s)/apiref/#(.+?)\)', f'{link_url_value_alter})', content, 1)
        current_link = re.search(r'(?s)\(/apiref/#(.+?)\)', content)
    content = re.sub(r'(?s)\(/apidocs/apiref/\)', r'(/api/)', content)
    return content


# for other link without /wep-content or /apiref, such as - [RankGame\_AutoJoinMatch](
# https://getbraincloud.com/apidocs/cloud-code-central/handy-cloud-code-scripts/rankgame_autojoinmatch/) we want to
# change it to  [RankGame\_AutoJoinMatch](/learn/cloud-code-central/handy-cloud-code-scripts/rankgame_autojoinmatch/)
def other_apidocs_link_process(content):
    content = re.sub(r'(?s)\(https://getbraincloud.com/apidocs/', r'(/apidocs/', content)
    content = re.sub(r'(?s)\(https://staging.getbraincloud.com/apidocs/', r'(/apidocs/', content)
    content = re.sub(r'(?s)\(/apidocs/', r'(/learn/', content)
    content = re.sub(r'(?s)\(/learn/tutorials', r'(/learn/sdk-tutorials', content)
    content = re.sub(r'(?s)\(/learn/introduction-2', r'(/learn/introduction', content)
    content = re.sub(r'(?s)\(/learn/api-reference-new', r'(/learn/api-reference', content)
    content = re.sub(r'(?s)\(/learn/api-modules', r'(/learn/key-concepts', content)
    content = re.sub(r'(?s)\(/learn/portal-usage', r'(/learn/portal-tutorials', content)
    content = re.sub(r'(?s)/cc-tutorial-4-pre-and-post-hooks', r'/cloud-code-tutorial4-pre-and-post-hooks', content)
    content = re.sub(r'(?s)/http-client-service', r'/cloud-code-tutorial5-external-web-service', content)
    content = re.sub(r'(?s)/s2s-cloud-code-scripts', r'/cloud-code-tutorial6-s2s-cloud-code-scripts', content)
    content = re.sub(r'(?s)/sdk-tutorials/c-tutorials', r'/sdk-tutorials/cpp-tutorials', content)
    content = re.sub(r'(?s)/capi/auth', r'/capi/authentication', content)
    content = re.sub(r'(?s)unity-tutorials/unity-tutorial-1-getting-started', r'unity-tutorials/unity-getting-started', content)
    content = re.sub(r'(?s)unreal-tutorials/getting-started-with-c/', r'unreal-tutorials/getting-started-with-cpp/',
                     content)
    return content


source_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/learn"
target_path = f"learn-copied"
# swap source and target to put change back, target is considered as temporary holder
# source_path = f"learn-output"
# target_path = f"learn"
if not os.path.isdir(target_path):
    os.mkdir(target_path)

files = os.scandir(source_path)

for file in files:
    s_level_1_folder_path = os.path.join(source_path, file.name)
    if os.path.isdir(file):
        t_level_1_folder = os.path.join(target_path, file.name)
        if file.name not in ['images', 'script']:
            if not os.path.isdir(t_level_1_folder):
                os.mkdir(t_level_1_folder)
            s_level_2_files = os.scandir(s_level_1_folder_path)
            for level_2_file in s_level_2_files:
                s_level_2_folder_path = os.path.join(s_level_1_folder_path, level_2_file.name)
                if os.path.isdir(level_2_file):
                    t_level_2_folder = os.path.join(t_level_1_folder, level_2_file.name)
                    if level_2_file.name not in ['images', 'script']:
                        if not os.path.isdir(t_level_2_folder):
                            os.mkdir(t_level_2_folder)
                        s_level_3_files = os.scandir(s_level_2_folder_path)
                        for level_3_file in s_level_3_files:
                            s_level_3_folder_path = os.path.join(s_level_2_folder_path, level_3_file.name)
                            if os.path.isdir(level_3_file):
                                t_level_3_folder = os.path.join(t_level_2_folder, level_3_file.name)
                                if level_3_file.name not in ['images', 'script']:
                                    if not os.path.isdir(t_level_3_folder):
                                        os.mkdir(t_level_3_folder)
                                    s_level_4_files = os.scandir(s_level_3_folder_path)
                                    for level_4_file in s_level_4_files:
                                        s_level_4_folder_path = os.path.join(s_level_3_folder_path, level_4_file.name)
                                        t_level_4_folder_path = os.path.join(t_level_3_folder, level_4_file.name)
                                        if os.path.isdir(level_4_file):
                                            shutil.copytree(s_level_4_folder_path, t_level_4_folder_path, ignore=shutil.ignore_patterns('*.md'))
                                        else:
                                            with open(level_4_file, 'r', encoding="Latin-1") as level_4_file_input:
                                                content = level_4_file_input.read()
                                                content = image_link_add_https_process(content)
                                                content = apiref_link_process(content)
                                                content = other_apidocs_link_process(content)
                                            with open(t_level_4_folder_path, 'w') as level_4_file_output:
                                                level_4_file_output.write(content)
                                else:
                                    shutil.copytree(s_level_3_folder_path, t_level_3_folder)
                            else:
                                with open(level_3_file, 'r') as level_3_file_input:
                                    content = level_3_file_input.read()
                                    content = image_link_add_https_process(content)
                                    content = apiref_link_process(content)
                                    content = other_apidocs_link_process(content)
                                with open(f'{t_level_2_folder}/{level_3_file.name}', 'w') as level_3_file_output:
                                    level_3_file_output.write(content)
                    else:
                        shutil.copytree(s_level_2_folder_path, t_level_2_folder)
                else:
                    with open(level_2_file, 'r') as level_2_file_input:
                        content = level_2_file_input.read()
                        content = image_link_add_https_process(content)
                        content = apiref_link_process(content)
                        content = other_apidocs_link_process(content)
                    with open(f'{t_level_1_folder}/{level_2_file.name}', 'w') as level_2_file_output:
                        level_2_file_output.write(content)
        else:
            shutil.copytree(s_level_1_folder_path, t_level_1_folder)
    else:
        with open(file, 'r') as level_1_file_input:
            content = level_1_file_input.read()
            content = image_link_add_https_process(content)
            content = apiref_link_process(content)
            content = other_apidocs_link_process(content)
        with open(f'{target_path}/{file.name}', 'w') as level_1_file_output:
            level_1_file_output.write(content)

# # sleep 5 seconds then write back to source from target
# time.sleep(5)
#
# source_path = f"learn-output"
# target_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/learn"
# if not os.path.isdir(target_path):
#     os.mkdir(target_path)
# files = os.scandir(source_path)
#
# for file in files:
#     s_level_1_folder_path = os.path.join(source_path, file.name)
#     if os.path.isdir(file):
#         if file.name not in ['images', 'script']:
#             t_level_1_folder = os.path.join(target_path, file.name)
#             if not os.path.isdir(t_level_1_folder):
#                 os.mkdir(t_level_1_folder)
#             s_level_2_files = os.scandir(s_level_1_folder_path)
#             for level_2_file in s_level_2_files:
#                 s_level_2_folder_path = os.path.join(s_level_1_folder_path, level_2_file.name)
#                 if os.path.isdir(level_2_file):
#                     if level_2_file.name not in ['images', 'script']:
#                         t_level_2_folder = os.path.join(t_level_1_folder, level_2_file.name)
#                         if not os.path.isdir(t_level_2_folder):
#                             os.mkdir(t_level_2_folder)
#                         s_level_3_files = os.scandir(s_level_2_folder_path)
#                         for level_3_file in s_level_3_files:
#                             s_level_3_folder_path = os.path.join(s_level_2_folder_path, level_3_file.name)
#                             if os.path.isdir(level_3_file):
#                                 if level_3_file.name not in ['images', 'script']:
#                                     t_level_3_folder = os.path.join(t_level_2_folder, level_3_file.name)
#                                     if not os.path.isdir(t_level_3_folder):
#                                         os.mkdir(t_level_3_folder)
#                                     with open(f'{s_level_3_folder_path}/index.md', 'r') as level_4_file_input:
#                                         content = level_4_file_input.read()
#                                     with open(f'{t_level_3_folder}/index.md', 'w') as level_4_file_output:
#                                         level_4_file_output.write(content)
#                             else:
#                                 with open(level_3_file, 'r') as level_3_file_input:
#                                     content = level_3_file_input.read()
#                                 with open(f'{t_level_2_folder}/{level_3_file.name}', 'w') as level_3_file_output:
#                                     level_3_file_output.write(content)
#                 else:
#                     with open(level_2_file, 'r') as level_2_file_input:
#                         content = level_2_file_input.read()
#                     with open(f'{t_level_1_folder}/{level_2_file.name}', 'w') as level_2_file_output:
#                         level_2_file_output.write(content)
#     else:
#         with open(file, 'r') as level_1_file_input:
#             content = level_1_file_input.read()
#         with open(f'{target_path}/{file.name}', 'w') as level_1_file_output:
#             level_1_file_output.write(content)
