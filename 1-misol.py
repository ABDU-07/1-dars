import os
id = 1
while 1:
    os.system("cls")
    f = open("Users_info.txt", "a+")
    name = input('Ism: ')
    lastname = input('Familya: ')
    i = 1; k = 1
    while 1:
        email_son = f.read().split()
        if i != 0:
            age = input('Yosh')
        if age.count('.') != 0:
              print("Notogri yosh: ")
        else:
            i = 0
        if i == 0 and k == 1:
            phone = input('Telfon nomer: ')
            if phone[:4] == '+998':
                if email_son.count(phone) == 0:
                    k = 0
                else:
                    print("Raqamdan avval foydalanilgan: ")
            else:
                print("Raqam Xato: ")
        if k == 0:
            email = input('email: ')
            if email[-10:] == '@gmail.com':
                if email_son.count(email) == 0:
                    break
                else:
                    print("Email mavjut: ")
            else:
                print("Email Xato: ")
    address = input('address')
    f.write(f"{id}: {name}\n   {lastname}\n   {str(age)}\n   {phone}\n   {email}\n   {address}\n\n")
    id += 1
f.close()