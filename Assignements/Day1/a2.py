'''
You are given a string .Your task is to find out if the string contains: 
    alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
      - expected outputs for all types or characters should be in boolean
'''

varString = input()

def var1():
    for i in varString:
        if(i.isalnum()):
            return True
    return False

def var2():
    for i in varString:
        if(i.isalpha()):
            return True
    return False
def var3():
    for i in varString:
        if(i.isdigit()):
            return True
    return False
def var4():
    for i in varString:
        if(i.islower()):
            return True
    return False
def var5():
    for i in varString:
        if(i.isupper()):
            return True
    return False
def var6():
    if var1() and var2() and var3() and var4() and var5():
        return True
    return False


varCheck = input("What do you want to validate: \n'1': alphanumeric characters\n'2': alphabetical characters\n'3': digits\n'4': lowercase\n'5': uppercase\n'6':All validations\n")
print("Great!! You have selected "+ varCheck +" Option.\n")
if varCheck == '1':
    print(var1())
elif varCheck == '2':
    print(var2())
elif varCheck == '3':
    print(var3())
elif varCheck == '4':
    print(var4())
elif varCheck == '5':
    print(var5())
elif varCheck == '6':
    print(var6())


'''
python3 a2.py
Swaraj123
6
'''