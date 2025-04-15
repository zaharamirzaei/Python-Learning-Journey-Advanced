#دیوار
import requests
import re
r=requests.get('https://divar.ir/s/mashhad')
print(r)
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
val=soup.find_all('div',attrs={'class': 'kt-post-card__body'})

for item in val:
    check=re.search(r'توافقی',item.text)
    if check==None:
        continue
    else:
        title=item.find('div',attrs={'class': 'kt-post-card__title'})
        print(title.text)
        
