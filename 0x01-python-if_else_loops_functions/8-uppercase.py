#!/usr/bin/python3
def uppercase(c):
    str1 = ""
    for i in c:
        num = ord(i)
        if num >= 97 and num <= 122:
            dif = num - 97
            new_num = 65 + diff
            str1 = str1 + chr(new_num)
        else:
            str1 = str1 + i
    print("{:s}".format(str1))
