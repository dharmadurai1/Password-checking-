import re
password=str(input("enter a password:ex,enter Abcde1@a"))
if (len(password)<8):
    print("password atleast have 8 charactors")
elif (re.search("[!@#$%^*]",password)is None):
    print("password have atleast one spacial charactor")
elif (re.search("[a-z]",password) is None):
    print("password atleast one small letter")
elif (re.search("[A-Z]",password)is None):
    print("password atleast one capital letters")
elif (re.search("[0-9]",password) is None):
    print("password atleast have one numeric ")
elif (re.search("[!2#%^&*a-zA-Z0-9]",password) is not None):
      print("valid password")
