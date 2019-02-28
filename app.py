u"""test web application module."""
from flask import Flask
from views.home import home_page
from views.test import v_test

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.register_blueprint(home_page)
app.register_blueprint(v_test)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
