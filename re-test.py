import json
import os
import re
import shutil

shutil.copytree('learn', 'test')

s = 'Make the 3 World a *Better Place*'
pattern = r'\*(.*?)\*'
replacement = r'<b>\1<\\b>'
html = re.sub(pattern, replacement, s)

print(html)

pattern = r'(\d+) (\w+)'
html = re.sub(pattern, r"2\ \1", s)

print(html)

txt = "The rain in Spain"
x = re.search("^The.*\sin", txt)

if x:
    print(type(x.group(0)))
else:
    print("No match")

# Replace the first two occurrences of a white-space character with the digit 9:

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)


txt = '''before the tag
1234
TAGS
this line will keep
this line will keep
this line will keep
TAGE
search text and pattern
bbb
ccc
'''
search = re.search(r"(?s)before.*TAGS", txt)
# print(search.group(0))

extract = re.search(r"(?s)TAGS.*TAGE", txt)
# print(extract.group(0))

# within one line
groupstest = re.search("search (.*) pattern", txt)
# search cross multilines
# groupstest = re.search("(?s)search(.*)ccc", txt)

# group(1) will return the 1st capture (stuff within the brackets).
# group(0) will return the entire matched text.
print(groupstest.group(1))
print(groupstest.group(0))

a = re.sub("(?s)before.*TAGS", "", txt)
print("sub result")
print(a)
b = re.sub("(?s)TAGE.*ccc", "", a)
# print(b)


data = [("B", 5, "20"), ("A", 1, "5"), ("C", 6, "10")]
# sort by the first value(letter) of tuples
data.sort(key=lambda x: x[0])

# print(data)


path = "./source_folder"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
# print the list
print(dir_list)
print(dir_list.sort())
print(dir_list)

proxy_name = re.sub(r'(?=[A-Z])', '-', "CustomEntity")
print(proxy_name)

# (?<!...) Matches if the current position in the string is not preceded by a match for .... This is called a
# negative lookbehind assertion. Similar to positive lookbehind assertions, the contained pattern must only match
# strings of some fixed length. Patterns which start with negative lookbehind assertions may match at the beginning
# of the string being searched.
proxy_name0 = re.sub(r'(?<!^)(?=[A-Z])', '-', "CustomEntity")
print(proxy_name0)

proxy_name1 = re.split(r'(?=[A-Z])', "customEntityFollowDDD FollowDDD")
print(proxy_name1)

# Empty matches for the pattern are replaced only when not adjacent to a previous empty match, so sub('x*', '-',
# 'abxd') returns '-a-b--d-'.
aa = re.sub('(?<!^)z*', '-', 'abxd')
print(aa)

# this is an interesting topic
# Read lines from one file and write to another file but remove lines that contain certain string
# https://stackoverflow.com/questions/11968998/read-lines-from-one-file-and-write-to-another-file-but-remove-lines-that-contain
# bad_words = ['bad', 'naughty']
#
# with open('oldfile.txt') as oldfile, open('newfile.txt', 'w') as newfile:
#     for line in oldfile:
#         if not any(bad_word in line for bad_word in bad_words):
#             newfile.write(line)

context = """
## Client API [capi]

Note that the client is normally managed via the <a href="#" onclick='window.navigateToTarget("#wrapper");'><code><%= data.branding.codeWrapper %></code></a> class

<aside class="notice">
<strong>MIN</strong> and <strong>MAX</strong> are really handy if your goal is to keep track of the highest-ever or lowest-ever value of a statistic.
</aside>

* <a href="#" onclick='window.navigateToTarget("#capi-authentication");'>Authentication</a>
* <a href="#" onclick='window.navigateToTarget("#capi-appstore");'>AppStore</a>
##### Bypassing ACL for System Objects
* [SysCreateEntity](#capi-customentity-syscreateentity) - Creates new custom entity.
* [SysDeleteEntity](#capi-customentity-sysdeleteentity) - Deletes the specified custom entity on the server.
* [SysDeleteEntities](#capi-customentity-sysdeleteentities) - Deletes all applicable custom entities from the server based on the custom entity type, specified delete criteria and acrossAllUsers flag.
* [SysGetCount](#capi-customentity-sysgetcount) - Counts the number of custom entities meeting the specified where clause.
* [SysGetEntityPage](#capi-customentity-sysgetentitypage) - Retrieves first page of custom entities from the server based on the custom entity type and specified query context
* [SysGetEntityPageOffset](#capi-customentity-sysgetentitypageoffset) - Gets the page of custom entities from the server based on the encoded context and specified page offset.
* [SysGetRandomEntitiesMatching](#capi-customentity-sysgetrandomentitiesmatching) - Gets a list of up to maxReturn randomly selected custom entities from the server based on the entity type and where condition, bypassing ownership/ACL permissions checking.
* [SysIncrementData](#capi-customentity-sysincrementdata) - Increments the specified fields by the specified amount within custom entity data on the server.
* [SysIncrementData](#capi-customentity-sysincrementdata) - Increments the specified fields by the specified amount within custom entity data on the server, bypassing ownership/ACL permissions checks.
* [SysIncrementDataSharded](#capi-customentity-sysincrementdatasharded) - Increments the specified fields by the specified amount within custom entity data on the server, bypassing ownership/ACL permissions.
* [SysReadEntity](#capi-customentity-sysreadentity) - Reads a custom entity.
* [SysUpdateEntity](#capi-customentity-sysupdateentity) - Replaces the specified custom entity's data, and optionally updates the acl and expiry, on the server.
* [SysUpdateEntityFields](#capi-customentity-sysupdateentityfields) - Sets the specified fields within custom entity data on the server.
* [SysUpdateEntityFieldsSharded](#capi-customentity-sysupdateentityfieldssharded) - For sharded custom collection entities. Sets the specified fields within custom entity data on the server, bypassing ACL permissions checks.
* [SysUpdateEntityOwner](#capi-customentity-sysupdateentityowner) - Updates the owner of the custom entity.


```objective_c
// Cloud Code only. To view example, switch to the Cloud Code tab
```

`
{
    "receipt": "ENCODED-RECEIPT-DATA"
}
`


<%= partial "partials/jsonBtn" %>

```json-doc
{
    "status": 200,
    "data": {}
}
```

<aside class="warning">
Make sure you've initialized the <%= data.branding.productName %> library before authenticating.
</aside>

<%= partial(:"partials/servop", :locals => { :service_name => "appStore", :operation_name => "RETURN_PURCHASE" }) %>

<%= partial "partials/errorHandlingBtn", :locals => {:language => 'csharp'} %>
```json-doc
{
    "status": 200,
    "data": {}
}
```
<%= partial(:"partials/versionTag", :locals => {
  :version => "4.5.0",
  :newText => "",
  :comingText => ""
}) %>


`
static const auto MAX_RESEND_INTERVAL = 500ms;
static const auto CHANNEL_HIGH_PRIORITY_1      = 0;
static const auto CHANNEL_HIGH_PRIORITY_2      = 1;
static const auto CHANNEL_NORMAL_PRIORITY      = 2;
static const auto CHANNEL_LOW_PRIORITY         = 3;
`

![Async Match Data Model](<%= I18n.t(:root) %> <%= data.images.asyncmatch %>)

#### Method Parameters
Parameter | Description
--------- | -----------
storeId | The store type - "itunes", "googlePlay", "amazon", "facebook" or "windows"
receiptData | A JSON object with data in the format for the specified store
"""


# replace single backtick with triple one
def replace_single_backtick(content):
    content = re.sub(r'\n`\n', r'\n```\n', content)
    return content


context = replace_single_backtick(context)


# replace aside note and keep origin class type as is
context = re.sub(r'<aside\sclass="(.+?)">', r':::\1', context)
context = re.sub(r'</aside>', ':::', context)

# take off jsonBtn
context = re.sub(r'<%= partial "partials/jsonBtn" %>', r'', context)


# replace img link
def img_link_process(content):
    content = re.sub(r'<%= I18n\.t\(:root\) %> <%= data\.images\.(.+?)\s%>', r'@site/docs/img/api-img/\1.png', content)
    return content


context = img_link_process(context)


# store code block then remove it from origin
def code_block_process(block_name, content):
    code_block = re.search(f'(?s)```{block_name}(.+?)```', content)
    if code_block:
        code_block_value = code_block.group(0)
        if block_name == "json-doc":
            code_block_value = re.sub(f'{block_name}', r'json', code_block_value)
        elif block_name == "objective_c":
            code_block_value = re.sub(f'{block_name}', r'objectivec', code_block_value)
        content = re.sub(f'(?s)```{block_name}(.+?)```', r'', content, 1)
    return {"code_block": code_block_value, "content": content}


# print(code_block_process("json-doc", context)['code_block'])
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


process_data = serv_op_process(context)
context = process_data['content']
# print(process_data['service_name'])
# print(process_data['operation_name'])

# get rid of version partial
context = re.sub(r'(?s)<%= partial\(:"partials/versionTag"(.+?)%>', r'', context)

# get rid of errorHandlingBtn partial
context = re.sub(r'(?s)<%= partial\s"partials/errorHandlingBtn"(.+?)%>', r'### Error Handling Example', context)


# # replace title to take off [] and set the title to h1 if it is h2
# def title_process(content):
#     title_text = re.search(r'##?\s(.+?)\[.+\]', content)
#     if title_text:
#         title_text_alter = re.sub(r'\[.+\]', '', title_text.group(0)).strip()
#         title_text_alter = re.sub(r'##?', '', title_text_alter).strip()
#         content = re.sub(r'##?\s(.+?)\[.+\]', f'# {title_text_alter}', content)
#     return content


# replace title to take off [] and set the title to h1 if it is h2
def title_process(content):
    title_text = re.search(r'##?\s(.+?)\n', content)
    if title_text:
        title_text_alter = re.sub(r'\[.+\]', '', title_text.group(0)).strip()
        title_text_alter = re.sub(r'##?', '', title_text_alter).strip()
        content = re.sub(r'##?\s(.+?)\[.+\]', '', content)
    return {"title": title_text_alter, "content": content}


# print(title_process(context)['title'])
context = title_process(context)['content']


# select method parameters block
# in case some files don't have a blank line at the end of method parameters block, add one here
param_block_value = ''
def param_block_process(content):
    content = content + "\n"
    global param_block_value
    param_block = re.search(r'(?s)#### Method(.+?)\n\n', content)
    if param_block:
        param_block_value = param_block.group(0)
        content = re.sub(r'(?s)#### Method(.+?)\n\n', '', content)
    return {"param_block": param_block_value, "content": content}


context = param_block_process(context)['content']

# set all h4, h5 level up two to h2, h3 accordingly
context = re.sub(r'####', r'##', context)


# find and replace anchor tag with internal file link
# e.g. <a href="#" onclick='window.navigateToTarget("#capi-authentication");'>Authentication</a>
# to [Authentication](/api/capi/authentication)
def anchor_process(content):
    current_anchor = re.search(r'(?s)<a href="#"(.+?)</a>', content)
    while current_anchor:
        link_text_search = re.search(r"(?s);'>(.+?)</a>", current_anchor.group(0))
        link_text_value = link_text_search.group(1).strip()
        link_url_search = re.search(r'(?s)\("#(.+?)"\)', current_anchor.group(0))
        link_url_value = link_url_search.group(1).strip()
        link_url_value_alter = "/api/" + re.sub(r'-', '/', link_url_value)
        content = re.sub(r"(?s)<a(.+?)</a>", f'[{link_text_value}]({link_url_value_alter})', content, 1)
        current_anchor = re.search(r"(?s)<a(.+?)</a>", content)
    return content


context = anchor_process(context)


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


context = internal_file_link_process(context)

print(context)


# # check file name if contain "__"
# if "__" in "filename__.md.erb":
#     print('found it')
# else:
#     print('not found')
#
#
# newContext = []
# for line in context:
#     if "line-delete-mark" in line:
#         print("line")
# print(newContext)
