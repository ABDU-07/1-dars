import os
os.system("cls")
f = open("Users_info.txt", "r+")

name = input()
lastname = input()
age = int(input())
if age.is_integer:
    True
else:
    False    

phone = input()
if phone.startswith("+998"):
    False
else: 
    True

email = input()
address = input()
f.writelines([name, "\n"])
f.writelines([lastname, "\n"])
f.writelines([str(age), "\n"])
f.writelines([phone, '\n'])
f.writelines([email, '\n'])
f.writelines([address,'\n'])

f.close()

    