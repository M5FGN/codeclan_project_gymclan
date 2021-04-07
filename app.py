from flask import Flask, render_template

from controllers.member_controller import members_blueprint
from controllers.gymsession_controller import gymsessions_blueprint
from controllers.booking_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(gymsessions_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/help')
def help():
    return render_template('help.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)