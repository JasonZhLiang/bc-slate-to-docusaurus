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
    content = re.sub(r'(?s)\(https://staging.getbraincloud.com/apidocs/wp-content/uploads/\d{4}/\d{2}/', r'(images/',
                     content)
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
    content = re.sub(r'(?s)/capi/auth/', r'/capi/authentication/', content)
    content = re.sub(r'(?s)unity-tutorials/unity-tutorial-1-getting-started', r'unity-tutorials/unity-getting-started',
                     content)
    content = re.sub(r'(?s)unreal-tutorials/getting-started-with-c/', r'unreal-tutorials/getting-started-with-cpp/',
                     content)
    return content


def move_status_code_to_json_response(content):
    status_code = re.search(r'(?s)### Status Codes(.+?)\n\n', content)
    if status_code:
        # content = re.sub(f'{status_code.group(0)}', f'', content, 1)
        content = re.sub(r'(?s)### Status Codes(.+?)\n\n', f'', content, 1)
        content = re.sub(f'</details>', f'</details>\n\n<details>\n<summary>Common Error Code</summary>\n\n{status_code.group(0)}</details>\n', content, 1)
    return content


source_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api"
target_path = f"api"

if not os.path.isdir(target_path):
    os.mkdir(target_path)


def process_folder(i_level, s_path, t_path):
    if os.path.isdir(s_path):
        files = os.scandir(s_path)
        if i_level > 0:
            for file in files:
                s_next_level_path = os.path.join(s_path, file.name)
                t_next_level_path = os.path.join(t_path, file.name)
                if os.path.isdir(file):
                    if file.name not in ['images', 'script']:
                        os.mkdir(t_next_level_path)
                    else:
                        shutil.copytree(s_next_level_path, t_next_level_path)
                elif '.md' in file.name:
                    with open(file, 'r') as file_input:
                        content = file_input.read()
                        content = image_link_add_https_process(content)
                        content = apiref_link_process(content)
                        content = other_apidocs_link_process(content)
                        content = move_status_code_to_json_response(content)
                    with open(t_next_level_path, 'w') as file_output:
                        file_output.write(content)
                else:
                    shutil.copy(s_next_level_path, t_next_level_path)
                process_folder(i_level - 1, s_next_level_path, t_next_level_path)
        else:
            return
    else:
        return


process_folder(5, source_path, target_path)
