# b = "a3b4c2e10b12"
b = open("source").read()
a = ''
c = ''
result_string = ''
for i in range(len(b)):
    # print(i)
    if b[i].isdigit() == False:
        if a != '':
            result_string = result_string + a * int(c)
            a = ''
            c = ''
        a = a + b[i]
        print(a)
    else:
        print(c)
        c = c + b[i]
    if i == len(b)-1:
        result_string = result_string + a * int(c)

# print(result_string)
open("result","w").write(result_string)