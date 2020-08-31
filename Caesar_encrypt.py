#askjdklasdja
b = int(input())
st = input().strip()
alf = ' abcdefghijklmnopqrstuvwxyz'
result = ''
if st.isdigit():
    print(f'Result: ""')
else:
    # if b >= len(alf):
    #     b = len(alf) - b
    # else:
    #     b = len(alf) + b
    for i in st:
        result = result + alf[(alf.find(i) + b) % len(alf)]
    print(f'Result: "{result}"')