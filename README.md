# PasswordStrengthAuditor
A password strength auditor written in Python. This program will prompt the user to enter a password. Then the password will be checked to see if it meets basic security criteria. After these checks are completed successfully, the entered password will be checked against a commonly used wordlist for dictionary attacks, rockyou.txt. 

For example, the password "PASSword123!!" passes all of the basic checks in the auditor, but will be rejected as it is contained within the rockyou.txt wordlist. The rockyou.txt wordlist can be downloaded from this github repository, https://github.com/RykerWilder/rockyou.txt/blob/main/rockyou.txt.zip

**Place rockyou.txt in the same folder as password_auditor.py before running the program.**

