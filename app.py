
from bs4 import BeautifulSoup
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


html= requests.get('https://www.worldometers.info/coronavirus/#countries').text
soup= BeautifulSoup(html,'lxml')

class data:
    def __init__(self,total,death,recover):
        self.total=total
        self.death=death
        self.recover=recover


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    msg=msg.upper()
    # Create reply
    table= soup.find('tbody')
    record={}
    
    for row in table.find_all('tr'):
        td = row.find_all('td')
        stat=[i.text for i in td]
        country= stat[0]
        count=stat[1]
        death= stat[3]
        rec=stat[5]
        country=country.upper()
        record[country]=data(count,death,rec)
    s= "total : " + record[msg].total + "/n" + "death : " + record[msg].death + "/n" + "recovered : " +  record[msg].recover
    resp = MessagingResponse()
    resp.message(s)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
