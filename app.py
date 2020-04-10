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
        death= stat[3]
        rec=stat[5]
        c=c-1
        t=0
        t+=count
        if(c>=0):
            s +=  "--> " + country + "\n" +" total  "+ count + "\n"  + "death " + death+ "\n" + "rec " + rec + " \n <--"
          
        if( country=="India" ):
            s+= "--> " + country +"\n" +"total "+ count +"\n" +"death "+ death+"\n" +"rec "+ rec +"\n <--"
         
        s+=" TOTAL "   +t + "\n"
         
    resp = MessagingResponse()
    resp.message(s)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
