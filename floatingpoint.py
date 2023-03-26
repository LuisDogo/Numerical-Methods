import math as m
# This program transforms decimal numbers to binary in the IEEE 754 form 32-bit floating point notation

string_num = input("Enter your decimal number: ")
sign = 0    # defined in lines 11:26
whole_num = 0 #assigned in lines 11:26
binary_num = [] #asssigned in lines 29:34
fraction_index = 0
fraction_num = 0


if(string_num[0] == '-'):
    sign = 1
    i = len(string_num)-2
    j = sign
    while(i>=0):
        if(string_num[j] == '.'):
            break
        whole_num += int(string_num[j]) * pow(10,i)
        i-=1
        j+=1
else:
    sign = 0
    i = len(string_num)-1
    j = sign
    while(i>=0):
        if(string_num[j] == '.'):
            break
        whole_num += int(string_num[j]) * pow(10,i)
        i-=1
        j+=1

print(whole_num)

while(whole_num/2>0):
    remainder = whole_num%2
    binary_num.append(remainder)
    whole_num = m.floor(whole_num/2)
binary_num.reverse()
print(binary_num)