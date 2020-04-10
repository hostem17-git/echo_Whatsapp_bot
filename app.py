from bs4 import BeautifulSoup
import requests

html= requests.get('https://www.worldometers.info/coronavirus/#countries').text
soup= BeautifulSoup(html,'lxml')

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    
    # Create reply
    table= soup.find('tbody')
    s=" "
    c=5
    for row in table.find_all('tr'):
        td = row.find_all('td')
        stat=[i.text for i in td]
        country= stat[0]
        count=stat[1]
        s+= country +" " + count +"\n"
        c=c-1
        if(c==0):
            break
    resp = MessagingResponse()
    resp.message(s)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=true)
    
