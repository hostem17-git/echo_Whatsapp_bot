
from bs4 import BeautifulSoup
#import urllib.request
import requests

html= requests.get('https://www.worldometers.info/coronavirus/#countries').text

soup= BeautifulSoup(html,'lxml')
#print(soup.prettify())

table= soup.find('tbody')

s=" "

for row in table.find_all('tr'):
    td = row.find_all('td')
    stat=[i.text for i in td]
    country= stat[0]
    count=stat[1]
    s+= country + " "+ count  + " \n"
    print(country," ",count)
    
print(s)
    
        
#print(table.prettify())
