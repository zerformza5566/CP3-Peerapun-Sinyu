usernameInput = input("Username : ")
passwordInput = input("Password : ")
passwordTry = 3

while usernameInput != "admin" or passwordInput != "1234" :
    passwordTry -= 1
    print("Incorrect Username or Password.")
    print(passwordTry, "try left.")
    if passwordTry == 0:
        print("Please wait for 15 minutes.")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")

print("Login completed.")