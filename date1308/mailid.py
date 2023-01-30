import re
s=input('Enter Mail id:')
m=re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.][a-z]+',s)

if m!=None:
    print("Valid Mail Id")
    
else:
    print("Invalid main id")