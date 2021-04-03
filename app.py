from flask import Flask, render_template

app = Flask(__name__)

from controllers import member_controller
from controllers import gymsession_controller
from controllers import booking_controller

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)