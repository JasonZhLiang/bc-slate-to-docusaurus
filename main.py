import json
import re

# proxy = input("enter proxy name: ").lower()
proxy = "start"
file_name_array = []
while proxy != "exit":
    proxy = input("enter proxy name: ").lower()
    try:
        with open(
                f"/Users/jasonl//bitbucket/braincloud-portal/Development/Server-AppServer/src/main/webapp/js/json/{proxy}.json",
                "r") as output:
            data = json.load(output)
    except FileNotFoundError:
        print("the proxy name your typed not exist!")
    else:
        proxy_name = re.sub(r'(?<!^)(?=[A-Z])', '-', data["serviceName"]).lower()
        print(proxy_name)
        file_name_array.append(f'"lib.cloudcode.{proxy_name}-service-proxy.d.ts"')
        with open("test/addForBridgeDTS.txt", "a") as globaldts:
            globaldts.write(f'\t/**\n')
            globaldts.write(f'\t * Retrieves a {data["serviceName"]}Service proxy object.\n')
            globaldts.write(f'\t * \n')
            globaldts.write(f'\t * @param session A optional parameter for when a script is executed without a session.\n')
            globaldts.write(f'\t */ \n')
            globaldts.write(f'\tget{data["serviceName"]}ServiceProxy(session?: string): {data["serviceName"]}ServiceProxy;\n\n')

        with open(f"lib.cloudcode.{proxy_name}-service-proxy.d.ts", "w") as file:
            file.write(f'/// <reference no-default-lib="true"/>\n\n')
            file.write(f'interface {data["serviceName"]}ServiceProxy {{\n')
            count = 0
            length = len(data["operations"])
            for method in data["operations"]:
                file.write(f'\t/**\n')
                file.write(f'\t * {method["desc"]}\n')
                file.write(f'\t * \n')
                param_string = ""
                try:
                    for param in method["paramInfo"]:
                        file.write(
                            f'\t * @param  {{{param["type"][0].lower() + param["type"][1:]}}} {param["name"]} {param["desc"]}\n')
                        param_string += f'{param["name"]}: {param["type"][0].lower() + param["type"][1:]}, '
                except KeyError:
                    print(f'no paramInfo for method {method["apiMethod"]}')

                file.write(f'\t * @returns ServiceProxyResponse\n')
                file.write(f'\t */ \n')
                method_name = method["apiMethod"][0].lower() + method["apiMethod"][1:]
                if param_string:
                    file.write(f'\t{method_name}({param_string[0:-2]}): ServiceProxyResponse;\n')
                else:
                    file.write(f'\t{method_name}(): ServiceProxyResponse;\n')
                count += 1
                if count < length:
                    file.write(f'\n')
            file.write('}')

print(file_name_array)
with open(f"dts_file_names", "w") as file_name:
    for i in file_name_array:
        file_name.write(f'{i},\n')
