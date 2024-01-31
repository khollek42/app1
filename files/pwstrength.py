password = input("Password must have a capital letter, a number, and 8-16 characters. \n"
    'Enter new password: ')

result = {}

if len(password) >= 8 and len(password) <= 16:
    result["length"] = True
else:
    result['length'] = False
digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

#prints dictonary results
#print(result)

if all(result.values()):
    print("Strong Password! ")
if result["length"] == False:
    print("Password is not between 8-16 characters.")
if result["digits"] == False:
    print("Password does not have number.")
if result["upper-case"] == False:
    print("Password does not have a capital letter.")
if all(result.values()) == False:
    print("Extremely Weak Password!!!Try Again @ IT!")
