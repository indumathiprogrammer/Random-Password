import random
print("Welcome To Random Password Generator")

randomchars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
nbrofpwd=int(input("Please Enter The Number Of Passwords To Be Generated: "))
pwdlen=int(input("Please Enter The Lengthen Of The Password Needed: "))

print("Here are your randome passwords:")
for x in range(nbrofpwd):
    pwd=""
    for chars in range(pwdlen):
        pwd=pwd+random.choice(randomchars)
    print(pwd)
