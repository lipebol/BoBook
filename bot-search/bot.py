from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from googlesearch import search

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    query01 = "amazon.com.br/Livros/" + incoming_msg
    result = []
    for sch in search(query01, tld='co.in', num=6, stop=6, pause=2):
        result.append(sch)
    msg.body(result[0])

    return str(resp)

if __name__ == '__main__':
   app.run()
