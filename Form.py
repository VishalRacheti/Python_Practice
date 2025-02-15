name = input ("Please enter the name")
email = input ("Please enter the email")
password = input ("Please enter the password")


if name == "":
    print ("Please enter the valid name ; cant be empty")
else:
    if "@" not in email :
        print("Please enter the valid email")

    else :
        if len(password) < 0 :
            print("No password entered ; enter valid password")

        else:
            print ("login/regrestration success")
