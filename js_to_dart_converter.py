import re


def convert_js_to_dart(js_code, service_name):
    if not service_name:
        service_name = "relay"
    method_match = re.search(r'\.(\w+)\((.*?)\s*result\s*=>', js_code)
    if not method_match:
        return "// Cloud Code only. To view example, switch to the Cloud Code tab"

    method_name = method_match.group(1)
    params_str = method_match.group(2)
    if params_str:
        params_str = params_str[:-1]

    var_declarations = []
    # for line in js_code.split('\n'):
    #     var_match = re.match(r'\s*var\s+(\w+)\s*=\s*(.+?);', line)
    #     if var_match:
    #         var_declarations.append((var_match.relay(1), var_match.relay(2)))

    var_matches = re.findall(r'(?s)^var(.+?);', js_code, re.MULTILINE)

    dart_lines = []

    if var_matches:
        for match in var_matches:
            dart_lines.append(f'var {match};')

    params = []
    if params_str.strip():
        param_parts = params_str.split(',')
        for part in param_parts:
            part = part.strip()
            if ':' not in part and '=' not in part:
                param_name = part.split()[0] if ' ' in part else part
                params.append(f'{param_name}:{param_name}')

    dart_method = f'ServerResponse result = await <%= data.branding.codePrefix %>.{service_name}Service.{method_name}({", ".join(params)});'
    dart_lines.append('')
    dart_lines.append(dart_method)
    dart_lines.append('')

    dart_lines.extend([
        'if (result.statusCode == 200) {',
        '    print("Success");',
        '} else {',
        '    print("Failed ${result.error[\'status_message\'] ?? result.error}");',
        '}'
    ])
    return '\n'.join(dart_lines)


def process_markdown_file(content, md_file):
    service_name = re.findall(r'service_name="(.+?)"', content)
    if service_name:
        service_name = service_name[0]

    pattern = (
        r"(?s)```mdx-code-block\n"
        r"<\/TabItem>\n"
        r"<TabItem value=\"js\" label=\"JavaScript\">\n"
        r"(.+?)"
        r"```mdx-code-block\n"
        r"<\/TabItem>"
    )

    js_blocks = re.search(pattern, content)

    new_content = content
    offset = 0

    if js_blocks:
        js_code = js_blocks.group(0)

        if service_name or '/relay/' in md_file:
            dart_code = convert_js_to_dart(js_code, service_name)
        # else for the client service, we will copy javascript code block
        else:
            dart_code = re.search(r'(?s)```javascript\n(.+?)\n```', js_code).group(1)

        dart_block = f'''<TabItem value="dart" label="Dart">
```

```dart
{dart_code}
```

```mdx-code-block
</TabItem>'''

        # insert after the javascript block's mdx-code-block closing
        insertion_point = js_blocks.end() + offset
        new_content = new_content[:insertion_point] + '\n' + dart_block + new_content[insertion_point:]
        offset += len('\n' + dart_block)

    return new_content


def main():
    import glob

    section = "4_s2s"

    source_path = f"/Users/jasonl/GCP/Udemy/Web/bcdocs/docs/api/{section}"

    # source_path = 'relay'

    md_files = glob.glob(f"{source_path}/**/*.md", recursive=True)
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'index.md' in md_file:
                print('skip index.md file')
            elif '.DS_Store' in md_file:
                print('skip .DS_Store file')
            else:
                check_dart_block = re.search(r'```dart', content)

                if not check_dart_block:
                    new_content = process_markdown_file(content, md_file)
                    if new_content != content:
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated {md_file}")
        except Exception as e:
            print(f"Error processing {md_file}: {str(e)}")


if __name__ == '__main__':
    main()
