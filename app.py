from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_time():
    now = datetime.now()
    return {
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second
    }

@app.route('/test_time')
def test_time():
    return {
        'hour': 23,
        'minute': 59,
        'second': 59
    }

if __name__ == '__main__':
    app.run(debug=True)