from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='/')

@app.route('/', methods=['GET'])
def home():
    return render_template("/homepage.html")

app.run()