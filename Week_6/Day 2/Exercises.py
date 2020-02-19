#Write a view that displays a greeting message to the user, this message should greet Good morning between 08:00 and 13:00,
# Good afternoon between 13:00 and 17:00, Good evening between 17:00 and 21:00 and Good night between 21:00 and 08:00.

from flask import Flask
from flask import render_template
from datetime import datetime, time

app = Flask(__name__)
@app.route('/')
def home():
    sentence = ""
    now = datetime.now()
    now_time = now.time()

    if now_time >= time(8) and now_time <= time(13):
        sentence = "Good morning"
    elif now_time >= time(13) and now_time <= time(17):
        sentence = "Good afternoon"
    elif now_time >= time(17) and now_time <= time(21):
        sentence = "Good evening"
    elif now_time >= time(21) and now_time <= time(8):
        sentence = "Good night"

    html = render_template('home1.html', greeting=sentence)
    return sentence

if __name__ == "__main__":

    app.run()



















































