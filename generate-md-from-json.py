import json
import re
import os


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
dart_head = """
```mdx-code-block
</TabItem>
<TabItem value="dart" label="Dart">
```
"""
lua_head = """
```mdx-code-block
</TabItem>
<TabItem value="lua" label="Roblox">
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

csharp_callback = """
SuccessCallback successCallback = (response, cbObject) =>
{
    Debug.Log(string.Format("Success | {0}", response));
};
FailureCallback failureCallback = (status, code, error, cbObject) =>
{
    Debug.Log(string.Format("Failed | {0}  {1}  {2}", status, code, error));
};
"""

java_callback = """
public void serverCallback(ServiceName serviceName, ServiceOperation serviceOperation, JSONObject jsonData)
{
    System.out.print(String.format("Success | %s", jsonData.toString()));
}
public void serverError(ServiceName serviceName, ServiceOperation serviceOperation, int statusCode, int reasonCode, String jsonError)
{
    System.out.print(String.format("Failed | %d %d %s", statusCode,  reasonCode, jsonError.toString()));
}
"""
dart_callback = """
if (result.statusCode == 200) {
    print("Success");
} else {
    print("Failed ${result.error['status_message'] ?? result.error}");
}
"""
lua_callback = """
if result.status == 200 then
    print("Success")
else
    print("Failed " .. tostring(result.error.status_message or result.error))
end
"""
# json or s2sJson
section = "json"
if section == "json":
    cloud_code_comment = "// Cloud Code only. To view example, switch to the Cloud Code tab"
else:
    cloud_code_comment = "// S2S call: to view example, switch to the Cloud Code or Raw tab."
store_folder = "./generated-md-files"
if not os.path.isdir(store_folder):
    os.mkdir(store_folder)
proxy = "start"
while proxy != "exit":
    proxy = input("enter proxy name: ").lower()
    try:
        with open(
                f"/Users/jasonl//bitbucket/braincloud-portal/Development/Server-AppServer/src/main/webapp/js/{section}/{proxy}.json",
                "r") as output:
            data = json.load(output)
    except FileNotFoundError:
        print("the proxy name your typed not exist!")
    else:
        operation_selection = input("method name ('all' -- entire methods that belong to the proxy your entered) : ").lower()
        # you can use wordninja to split all lowercase without space words string split into a words array
        # wordninja.split('getcatalogitemspagetoseparate') to ['get', 'catalog', 'items', 'page', 'to', 'separate']
        # then use ' '.join(['get', 'catalog', 'items', 'page', 'to', 'separate']).title().replace(' ', '') change it to
        # GetCatalogItemsPageToSeparate to compare with apiMethod value
        # or simply just convert apiMehod to lower() compare with your input
        if operation_selection == 'all':
            for operation in data["operations"]:
                with open(f'{store_folder}/{operation["apiMethod"].lower()}.md', 'w') as api_method:
                    api_method.write(f'# {operation["apiMethod"]}\n')
                    # api_method.write(f'## Overview\n')
                    api_method.write(f'{operation["desc"]}\n\n')
                    api_method.write(f'<PartialServop service_name="{operation["service"]}" operation_name="{operation["serviceOperation"]}" />\n\n')
                    # writing method parameters
                    if "paramInfo" in operation:
                        api_method.write(f'## Method Parameters\n')
                        api_method.write(f'Parameter | Description\n--------- | -----------\n')
                        for param in operation["paramInfo"]:
                            api_method.write(f'{param["name"]} | {param["desc"]}\n')
                        api_method.write(f'\n')
                    # writing Usage section
                    api_method.write(f'## Usage\n')
                    if operation["apiMethod"].startswith('Sys'):
                        api_method.write(f'{csharp_head}\n')
                        api_method.write(f'```csharp\n')
                        api_method.write(f'{cloud_code_comment}\n')
                        api_method.write(f'```\n')
                        api_method.write(f'{cpp_head}\n')
                        api_method.write(f'```cpp\n')
                        api_method.write(f'{cloud_code_comment}\n')
                        api_method.write(f'```\n')
                        api_method.write(f'{objective_c_head}\n')
                        api_method.write(f'```objectivec\n')
                        api_method.write(f'{cloud_code_comment}\n')
                        api_method.write(f'```\n')
                        api_method.write(f'{java_head}\n')
                        api_method.write(f'```java\n')
                        api_method.write(f'{cloud_code_comment}\n')
                        api_method.write(f'```\n')
                        api_method.write(f'{javascript_head}\n')
                        api_method.write(f'```javascript\n')
                        api_method.write(f'{cloud_code_comment}\n')
                        api_method.write(f'```\n')
                        api_method.write(f'{dart_head}\n')
                        api_method.write(f'```dart\n')
                        api_method.write(f'{cloud_code_comment}\n')
                        api_method.write(f'```\n')
                        api_method.write(f'{lua_head}\n')
                        api_method.write(f'```lua\n')
                        api_method.write(f'{cloud_code_comment}\n')
                        api_method.write(f'```\n')
                    else:
                        # csharp block
                        api_method.write(f'{csharp_head}\n')
                        api_method.write(f'```csharp\n')
                        if "paramInfo" in operation:
                            param_list = []
                            for param in operation["paramInfo"]:
                                if param['type'] == 'String':
                                    api_method.write(f'string {param["name"]} = "{operation["parameters"][param["name"]]}";\n')
                                elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                    convert_json = re.sub(r'\n', '', str(operation["parameters"][param["name"]]))
                                    convert_json = re.sub(f"'", '\\"', convert_json)
                                    api_method.write(f'string {param["name"]} = "{convert_json}";\n')
                                elif param['type'] == 'Boolean':
                                    api_method.write(f'bool {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Long':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Integer':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                else:
                                    api_method.write(f'var {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                param_list.append(param["name"])
                            param_list_string = ', '.join(param_list)
                            api_method.write(f'{csharp_callback}\n')
                            api_method.write(f'<%= data.branding.codePrefix %>.{operation["service"].title()}Service.{operation["apiMethod"]}({param_list_string}, successCallback, failureCallback);\n')
                        else:
                            api_method.write(f'{csharp_callback}\n')
                            api_method.write(f'<%= data.branding.codePrefix %>.{operation["service"].title()}Service.{operation["apiMethod"]}(successCallback, failureCallback);\n')
                        api_method.write(f'```\n')
                        # cpp block
                        api_method.write(f'{cpp_head}\n')
                        api_method.write(f'```cpp\n')
                        if "paramInfo" in operation:
                            param_list = []
                            for param in operation["paramInfo"]:
                                if param['type'] == 'String':
                                    api_method.write(f'const char *{param["name"]} = "{operation["parameters"][param["name"]]}";\n')
                                elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                    convert_json = re.sub(r'\n', '', str(operation["parameters"][param["name"]]))
                                    convert_json = re.sub(f"'", '\\"', convert_json)
                                    api_method.write(f'const char *{param["name"]} = "{convert_json}";\n')
                                elif param['type'] == 'Boolean':
                                    api_method.write(f'bool {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Long':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Integer':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                else:
                                    api_method.write(f'var {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                param_list.append(param["name"])
                            param_list_string = ', '.join(param_list)
                            api_method.write(f'<%= data.branding.codePrefix %>.get{operation["service"].title()}Service().{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}({param_list_string}, this);\n')
                        else:
                            api_method.write(f'<%= data.branding.codePrefix %>.get{operation["service"].title()}Service().{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}(this);\n')
                        api_method.write(f'```\n')
                        # objective-c block
                        api_method.write(f'{objective_c_head}\n')
                        api_method.write(f'```objectivec\n')
                        if "paramInfo" in operation:
                            param_list = []
                            for param in operation["paramInfo"]:
                                if param['type'] == 'String':
                                    api_method.write(f'NSString *{param["name"]} = @"{operation["parameters"][param["name"]]}";\n')
                                elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                    convert_json = re.sub(r'\n', '', str(operation["parameters"][param["name"]]))
                                    convert_json = re.sub(f"'", '\\"', convert_json)
                                    api_method.write(f'NSString *{param["name"]} = @"{convert_json}";\n')
                                elif param['type'] == 'Boolean':
                                    api_method.write(f'BOOL {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Long':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Integer':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                else:
                                    api_method.write(f'var {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                param_list.append(param["name"])
                            api_method.write(f'BCCompletionBlock successBlock; // define callback\nBCErrorCompletionBlock failureBlock; // define callback\n')
                            api_method.write(f'[[<%= data.branding.codePrefix %> {operation["service"]}Service] {operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}:'.rjust(40)+'\n')
                            for param_name in param_list:
                                api_method.write(f'{param_name}:'.rjust(30) + f'{param_name}\n')
                            api_method.write(f'completionBlock:'.rjust(30) + f'successBlock\n')
                            api_method.write(f'errorCompletionBlock:'.rjust(30) + f'failureBlock\n')
                            api_method.write(f'cbObject:'.rjust(30) + f'nil]\n')
                        else:
                            api_method.write(
                                f'BCCompletionBlock successBlock; // define callback\nBCErrorCompletionBlock failureBlock; // define callback\n')
                            api_method.write(
                                f'[[<%= data.branding.codePrefix %> {operation["service"]}Service] {operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}:'.rjust(
                                    40) + '\n')
                            api_method.write(f'completionBlock:'.rjust(30) + f'successBlock\n')
                            api_method.write(f'errorCompletionBlock:'.rjust(30) + f'failureBlock\n')
                            api_method.write(f'cbObject:'.rjust(30) + f'nil]\n')
                        api_method.write(f'```\n')
                        # java block
                        api_method.write(f'{java_head}\n')
                        api_method.write(f'```java\n')
                        if "paramInfo" in operation:
                            param_list = []
                            for param in operation["paramInfo"]:
                                if param['type'] == 'String':
                                    api_method.write(f'String {param["name"]} = "{operation["parameters"][param["name"]]}";\n')
                                elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                    convert_json = re.sub(r'\n', '', str(operation["parameters"][param["name"]]))
                                    convert_json = re.sub(f"'", '\\"', convert_json)
                                    api_method.write(f'String {param["name"]} = "{convert_json}";\n')
                                elif param['type'] == 'Boolean':
                                    api_method.write(f'bool {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Long':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                elif param['type'] == 'Integer':
                                    api_method.write(f'int {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                else:
                                    api_method.write(f'var {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                param_list.append(param["name"])
                            api_method.write(f'this; // implements IServerCallback\n')
                            param_list_string = ', '.join(param_list)
                            api_method.write(f'<%= data.branding.codePrefix %>.get{operation["service"].title()}Service.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}({param_list_string}, this);\n')
                        else:
                            api_method.write(f'this; // implements IServerCallback\n')
                            api_method.write(f'<%= data.branding.codePrefix %>.get{operation["service"].title()}Service.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}(this);\n')
                        api_method.write(f'{java_callback}')
                        api_method.write(f'```\n')
                        # javascript block
                        api_method.write(f'{javascript_head}\n')
                        api_method.write(f'```javascript\n')
                        if "paramInfo" in operation:
                            param_list = []
                            for param in operation["paramInfo"]:
                                if param['type'] == 'String':
                                    api_method.write(
                                        f'var {param["name"]} = "{operation["parameters"][param["name"]]}";\n')
                                elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                    api_method.write(
                                        f'var {param["name"]} = {json.dumps(operation["parameters"][param["name"]], indent=4)};\n')
                                else:
                                    api_method.write(
                                        f'var {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                param_list.append(param["name"])
                            param_list_string = ', '.join(param_list)
                            api_method.write(f'<%= data.branding.codePrefix %>.{operation["service"]}.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}({param_list_string}, result =>\n{{\n  var status = result.status;\n  console.log(status + " : " + JSON.stringify(result, null, 2));\n}});\n')
                        else:
                            api_method.write(f'<%= data.branding.codePrefix %>.{operation["service"]}.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}(result =>\n{{\n  var status = result.status;\n  console.log(status + " : " + JSON.stringify(result, null, 2));\n}});\n')
                        api_method.write(f'```\n')
                        # dart block
                        api_method.write(f'{dart_head}\n')
                        api_method.write(f'```dart\n')
                        if "paramInfo" in operation:
                            param_list = []
                            for param in operation["paramInfo"]:
                                if param['type'] == 'String':
                                    api_method.write(
                                        f'var {param["name"]} = "{operation["parameters"][param["name"]]}";\n')
                                elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                    api_method.write(
                                        f'var {param["name"]} = {json.dumps(operation["parameters"][param["name"]], indent=4)};\n')
                                else:
                                    api_method.write(
                                        f'var {param["name"]} = {operation["parameters"][param["name"]]};\n')
                                param_list.append(param["name"])

                            param_list_string = ""
                            for param_name in param_list:
                                param_list_string += f'{param_name}:{param_name}, '
                            api_method.write(f'ServerResponse result = await <%= data.branding.codePrefix %>.{operation["service"]}Service.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}({param_list_string[0:-2]});\n')
                        else:
                            api_method.write(f'ServerResponse result = await <%= data.branding.codePrefix %>.{operation["service"]}Service.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}();\n')
                        api_method.write(f'{dart_callback}')
                        api_method.write(f'```\n')
                        # lua block
                        api_method.write(f'{lua_head}\n')
                        api_method.write(f'```lua\n')
                        if "paramInfo" in operation:
                            param_list = []
                            for param in operation["paramInfo"]:
                                if param['type'] == 'String':
                                    api_method.write(
                                        f'local {param["name"]} = "{operation["parameters"][param["name"]]}"\n')
                                elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                    lua_table = json.dumps(operation["parameters"][param["name"]], indent=4)
                                    lua_table = re.sub(r'"(\w+)"(\s*):', r'\1\2=', lua_table)
                                    lua_table = re.sub(r'\bnull\b', 'nil', lua_table)
                                    api_method.write(
                                        f'local {param["name"]} = {lua_table}\n')
                                elif param['type'] == 'Boolean':
                                    api_method.write(
                                        f'local {param["name"]} = {str(operation["parameters"][param["name"]]).lower()}\n')
                                elif param['type'] == 'Long' or param['type'] == 'Integer':
                                    api_method.write(
                                        f'local {param["name"]} = {operation["parameters"][param["name"]]}\n')
                                else:
                                    api_method.write(
                                        f'local {param["name"]} = {operation["parameters"][param["name"]]}\n')
                                param_list.append(param["name"])
                            param_list_string = ', '.join(param_list)
                            api_method.write(f'<%= data.branding.codePrefix %>.{operation["service"]}Service:{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}({param_list_string})\n')
                        else:
                            api_method.write(f'<%= data.branding.codePrefix %>.{operation["service"]}Service:{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}()\n')
                        api_method.write(f'{lua_callback}')
                        api_method.write(f'```\n')
                    # left indent one level higher than code blocks above, no matter sys or non-sys calls
                    # cfs block
                    api_method.write(f'{cfs_head}\n')
                    api_method.write(f'```cfscript\n')
                    if "paramInfo" in operation:
                        param_list = []
                        for param in operation["paramInfo"]:
                            if param['type'] == 'String':
                                api_method.write(f'var {param["name"]} = "{operation["parameters"][param["name"]]}";\n')
                            elif param['type'] == 'NativeObject' or param['type'] == 'NativeArray':
                                api_method.write(f'var {param["name"]} = {json.dumps(operation["parameters"][param["name"]], indent=4)};\n')
                            else:
                                api_method.write(f'var {param["name"]} = {operation["parameters"][param["name"]]};\n')
                            param_list.append(param["name"])
                        param_list_string = ', '.join(param_list)
                        api_method.write(f'var {operation["service"]}Proxy = bridge.get{operation["service"].title()}ServiceProxy();\n')
                        api_method.write(f'\nvar postResult = {operation["service"]}Proxy.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}({param_list_string});\n')
                    else:
                        api_method.write(
                            f'var {operation["service"]}Proxy = bridge.get{operation["service"].title()}ServiceProxy();\n')
                        api_method.write(
                            f'\nvar postResult = {operation["service"]}Proxy.{operation["apiMethod"][0].lower() + operation["apiMethod"][1:]}();\n')
                    api_method.write(f'```\n')
                    # r block
                    api_method.write(f'{r_head}\n')
                    api_method.write(f'```r\n')
                    if "paramInfo" in operation:
                        new_dict = {
                            "service": operation["service"],
                            "operation": operation["serviceOperation"],
                            "data": operation["parameters"]
                        }
                    else:
                        new_dict = {
                            "service": operation["service"],
                            "operation": operation["serviceOperation"]
                        }
                    api_method.write(json.dumps(new_dict, indent=4, separators=(",", ":")))
                    api_method.write(f'\n')
                    api_method.write(f'```\n')
                    # ending code block
                    api_method.write(f'{block_end}')
                    # writing json response
                    api_method.write(f'<details>\n<summary>JSON Response</summary>\n\n')
                    api_method.write(f'```json\n{{\n  "status" : 200,\n  "data" : {{}}\n}}\n```\n\n')
                    api_method.write(f'</details>\n')


