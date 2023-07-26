# we will tell the user only if the password is correct

password = input("Enter password: ")
while password != "pass123":
    password = input("Wrong! Enter password the correct password: ")

print("Password is correct")