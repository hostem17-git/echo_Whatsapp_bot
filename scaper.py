from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup= BeautifulSoup(html_file,'lxml')

#print(soup.prettify())

match= soup.title.text# gices first title tag

#match= soup.title  <- prints tags too
# to print just the tag use "text attribute" as shown above

print(match)


''' we use soup.find to search for tags with specific properties'''
# we need _ after class bcoz its a python keyword too

'''find method returns the first occurence''' 


#match= soup.find('div',class_='footer')
#print(match.text)


'''find_all returns a list of all occurences, use for loop to go through them all'''

for article in soup.find_all('div',class_='article'):
    '''find article 1'''
    ''' once found the designated div, use"." to access members in the same order as they are coded'''
    #article=soup.find('div',class_='article')
    headline=article.h2.a.text
    print(headline)
    summary=article.p.text
    print(summary)
    print()
