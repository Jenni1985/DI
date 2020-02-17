from flask import Flask

#Create Flask app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, !'

@app.route('/home/<string:name>')
def home(name):
    html =  f''< h1 style= 'color: red;' >'' Welcome (name) </ h1 >''
    return html


#Start the app
app.run()

