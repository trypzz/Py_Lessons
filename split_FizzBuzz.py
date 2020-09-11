# b = input()
b = "a2z12E16P18S14P6j8P6r11A3r12n16U7r2b15Y20u17Z13q9O17S7G13J2d20v11u18t6Z12T8"
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
