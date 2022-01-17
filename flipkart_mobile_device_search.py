#step 0: install required modules
import requests
import xlsxwriter
from bs4 import BeautifulSoup

mobile=input("enter mobile name: ")
page=int(input('enter no of pages'))

#defining excel workbook 
workbook = xlsxwriter.Workbook(mobile+'.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0

try:
    for p in range(1,page+1):
        pg=str(p)
        url='https://www.flipkart.com/search?q='+mobile+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+pg
        r=requests.get(url)
        htmlcontent=r.content
        soup=BeautifulSoup(htmlcontent, "lxml")
        data=soup.find_all('div', class_='_2kHMtA')
        
        #iterating though all the products
        for d in data:
            name=d.find('div', class_='_4rR01T').string
            price=d.find('div',class_='_30jeq3 _1_WHN1').string.replace('₹','Rs').replace(',','')
            l=d.find('a',class_='_1fQZEK')
            product=name+" "+price
            print(str(product))

            #creating excel sheet
            worksheet.write(row, column, name)
            worksheet.write(row, column+1, price.replace('Rs',''))
            worksheet.write(row, column+2, 'www.flipkart.com'+l['href'])
            row += 1      
             
except:
    print("URL not able to connect")
workbook.close() 


    





 


     
