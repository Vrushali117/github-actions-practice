#this is sample python code
from flask import Flask, render_template
app = Flask(name)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
