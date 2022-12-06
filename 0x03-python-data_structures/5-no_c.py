#!/usr/bin/python3
def no_c(str):
    newstr = ""
    
    if str == None:
        return None
    for i in str:
        if i == 'c' or i == 'C':
            continue
        newstr += i
    return newstr

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
print(no_c(""))
