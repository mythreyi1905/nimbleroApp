from flask import Flask,render_template, session,redirect
from functools import wraps
import pymongo 
app = Flask(__name__)
app.secret_key = b'$*\xc2\x81\xe3\xb3b\x05\xe9I\x916m\xcb\xd0\x17'
client = pymongo.MongoClient('localhost',27017)
db = client.user_login_system

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            return redirect('/')
    
    return wrap


from user import routes
from user.routes import readMessage

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    messages = readMessage()
    return render_template('dashboard.html',messages = messages)

@app.route('/user/readMessage')
@login_required
def message():
    return render_template('messages.html')

