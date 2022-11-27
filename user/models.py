from flask import Flask,jsonify, request,session , redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
from datetime import datetime
now = datetime.now() # current date and time

class User:

    def login(self):
        user = db.users.find_one({"email": request.form.get('email')})
        if user and pbkdf2_sha256.verify(request.form.get('password'),user['password']):
            return self.start_session(user)
        return jsonify({"error":"Invalid login credentials"}),401

    def start_session(self,user):
        del user['password']
        session['logged_in'] = True
        session['user']=user
        return jsonify(user),200

    def signup(self):
        print(request.form)
        user = {
            "_id":uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        if db.users.find_one({"email":user['email']}):
            return jsonify({"error":"Email address already in use"}),400
        if db.users.insert_one(user):
            return self.start_session(user)
        return jsonify({"error":"Signup failed"}),400
    
    def signout(self):
        session.clear()
        return redirect('/')

    def sendMessage(self):
        user = db.users.find_one({"email": request.form.get('email')})
        print(user)
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        if user:
            message = {
            "_id":uuid.uuid4().hex,
            "email":request.form.get('email'),
            "message":request.form.get('message'),
            "sender":session['user']['email'],
            "timestamp":date_time
            }
            db.messages.insert_one(message)
            return jsonify(message)
        return jsonify({"error":"Invalid user"}),401
        
    def readMessage(self):
        messages =[]
        message = db.messages.find({"email": session['user']['email']})
        for i in message:
            messages.append(i)
        print(messages)
        print("Im here")
        return messages
    
        