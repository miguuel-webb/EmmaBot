from flask import Flask 
from threading import Thread

app = Flask('')

@app.route('/')
def index():
    return 'hello form Flask!'

def run():
    app.run(host='127.0.0.1', port=8000)

def comandodeinicio():
    server=Thread(target=run)
    server.start()
