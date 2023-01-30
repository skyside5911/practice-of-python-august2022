#to find the mobile number is valid or not
import re
number=input('enter the number to find it is validate or not ')
matchh=re.fullmatch('[6-9]\d{9}',number)
if matchh !=None:
    print(number,"  is valid number ")
else:
    print(number," is not valid number ")