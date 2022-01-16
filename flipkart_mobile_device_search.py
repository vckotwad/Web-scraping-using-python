#step 0: install required modules
import requests
from bs4 import BeautifulSoup
try:
    mobile=input("enter mobile brand- ")
    url='https://www.flipkart.com/search?q='+mobile+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    r=requests.get(url)
    htmlcontent=r.content
    soup=BeautifulSoup(htmlcontent, "lxml")
    data=soup.find_all('div', class_='_2kHMtA')
    for d in data:
        print("product name: ",d.find('div', class_='_4rR01T').string)
        print("price:-",d.find('div',class_='_30jeq3 _1_WHN1').string)
        print()    
except:
    print("URL not able to connect")
