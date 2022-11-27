## Chat / Messaging Application 

Front end : HTML, CSS
Back end ; Flask
Database : MongoDB


## Pre-requisite : 
MongoDB - Preferably version 6.0.1 running on port 27017

## Steps to run: 

In order to run this application locally, clone this repository on your machine and cd into `nimbleroApp` 

If you do not have virtualenv installed on your machine, install it using the following command: 

`python3 -m pip install --user virtualenv`

Create a virtual environment using the following command: 

`python3 -m venv env`

Activate the virtual environment using the following command: 

`source env/bin/activate`

Once you have activated the virtual environment, run the following command to install dependencies: 

`pip install flask pymongo passlib`

Now run the application using the following command:
`./run`

Once the application has started,visit `http://127.0.0.1:5000/` on your browser to access the application

[Youtube link](https://youtu.be/wolCMT1NsyQ)








