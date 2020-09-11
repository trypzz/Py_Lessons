import requests

with open("3.6.1/source", 'w+') as f:
    s = requests.get("https://stepic.org/media/attachments/course67/3.6.2/289.txt").text
    count = 0
    f.write(s)
# f.write(s)
for i in s.splitlines():
    count += 1
print(count)
