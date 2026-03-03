import json
import os
import re
import shutil

# shutil.copytree('learn', 'test')

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
    print(x.group(0))
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

# (?s) re.DOTALL (inline flag) -- Make the '.' special character match any character at all, including a newline
search = re.search(r"(?s).*TAGS", txt)
print(search)
print(search.group(0))

extract = re.search(r"(?s)TAGS.*TAGE", txt)
# print(extract.relay(0))
print("-----------extract------------------")
print(extract.start())
print(extract.end())
print(extract.span())

# within one line
groupstest = re.search("search (.*) pattern", txt)
# search cross multilines
# groupstest = re.search("(?s)search(.*)ccc", txt)

# relay(1) will return the 1st capture (stuff within the brackets).
# relay(0) will return the entire matched text.
# print(groupstest.relay(1))
# print(groupstest.relay(0))

a = re.sub("(?s)before.*TAGS", "", txt)
print("sub result")
print(a)
b = re.sub("(?s)TAGE.*ccc", "", a)
print(b)


data = [("B", 5, "20"), ("A", 1, "5"), ("C", 6, "10")]
# sort by the first value(letter) of tuples
data.sort(key=lambda x: x[0])
