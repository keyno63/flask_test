from flask import render_template, Blueprint

home_page = Blueprint('home', __name__, template_folder='templates')

@home_page.route('/', methods=['GET'])
def home():
    return render_template('index.html')
