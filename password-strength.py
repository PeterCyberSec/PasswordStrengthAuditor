print("-----Password Auditor-----")
while True: #Loop until a strong enough password is entered
    password = input("Enter password: ") #Receive the user's password
    Strong= False #Will be true when password is strong enough
    Caps = False
    Lower = False
    Numeric = False
    Special = False
    Space = False
    if len(password) >= 12: #Begin other checks if password is long enough
        for i in password: #Iterate through each character of the password
            if i.isspace(): #Is character a space?
                Space = True
            elif i.isupper(): #Is character an uppercase letter?
                Caps = True 
            elif i.islower(): #Is character a lowercase letter?
                Lower = True
            elif i.isnumeric(): #Is character a number?
                Numeric = True
            else: # If character is not a letter, number, or space, then it must be a special character
                Special = True
        if Space: 
            print("Passwords cannot contain spaces")
        if not Caps:
            print("Passwords must contain at least 1 upper case letter") 
        if not Lower:
            print("Passwords must contain at least 1 lower case letter")
        if not Numeric:
            print("Passwords must contain at least 1 number")
        if not Special:
            print("Passwords must contain at least 1 special character")  
        if Caps and Lower and Numeric and Special and not Space: #If all criteria checks have passed successfully
            with open("rockyou.txt", encoding="latin-1") as f: #Open the rockyou wordlist
                for x in f:
                    if password == x.strip(): #If password is found in rockyou wordlist
                        print("Password is too common - discovered in a wordlist")
                        Strong = False
                        break
                else: #If password isn't in wordlist then it is strong enough
                    print("Password is strong enough")
                    Strong = True
        if Strong:
            break

    elif len(password) == 0: #Check that something was actually entered
        print("Please enter a password") 
    else: #If password is shorter than 12 characters        
        print("Password must contain at least 12 characters")