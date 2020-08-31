b = input()
a = ''
result_string = ''
for i in b:
    # print(i)
    if i.isdigit():
        a = a + i
    else:
        if a == '':
            result_string = result_string + i
        else:
            result_string = result_string + int(a) * i
            a = ''
print(result_string)
