import requests
stop = ['1']
URL = "https://stepic.org/media/attachments/course67/3.6.3/"
f = "699991.txt"
while stop[0] != 'We':
    s = requests.get(URL+f).text
    print(s)
    f = s
    txt = open('URL','w')
    txt.write(s)
    stop = s.split()
    print(stop)
