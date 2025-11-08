import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

responses = {
    "hello": "Hello 👋 Welcome to Infuzio Bahawalpur! Type Menu, Location, or Hours to get started.",
    "menu": "Here’s our latest menu PDF 🍽️ https://drive.google.com/file/d/1sgukSXZrNghsPXrA45gBaYF0x7CmaC6Z/view?usp=drive_link",
    "location": "📍 We’re located at Street 7, Gulberg Road, Bahawalpur. Open map: https://maps.app.goo.gl/mrVR4U2MBrQQ1dJN7",
    "hours": "🕒 Opening Hours: 12 PM – 12 AM"
}

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    reply_text = responses.get(incoming_msg, 
        "Sorry, I didn’t understand that. Type Hello, Menu, Location, or Hours.")
    
    resp = MessagingResponse()
    resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

