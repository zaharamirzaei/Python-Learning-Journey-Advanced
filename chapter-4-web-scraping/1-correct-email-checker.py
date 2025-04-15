#ایمیل صحیح
import re
email=input()
check=re.search(r'^\w+\@[A-z]+\.[A-z]+$',email)
if check==None:
    print("WRONG")
else:
    print("OK")
