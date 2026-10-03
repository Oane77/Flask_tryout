from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Hallo, ik heb les 11 doorlopen.</p>"
