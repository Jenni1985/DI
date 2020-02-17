import datetime
From flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/index")
def today():
    now = datetime.datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    html = ''''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test</title>
</head>
<body>
 Today is {16/02/2020}
</body>
</html>'''
    return html


app.run()
