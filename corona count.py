
from bs4 import BeautifulSoup
import urllib.request
import requests

html= requests.get('https://www.worldometers.info/coronavirus/#countries').text

'''
with urllib.request.urlopen('https://www.worldometers.info') as response:
    html= response.read()
'''
soup= BeautifulSoup(html,'lxml')
#print(soup.prettify())

table= soup.find('tbody')


for row in table.find_all('tr'):
    td = row.find_all('td')
    stat=[i.text for i in td]
    country= stat[0]
    count=stat[1]
    print(country," ",count)
    
    
        
#print(table.prettify())
