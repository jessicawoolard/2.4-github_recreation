

from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():

    response = requests.get('https://api.github.com/users/jessicawoolard')

    data = response.json()
    # print(data)

    github_infomation = data['login']
    print(github_infomation)




# @app.route('/repos')

# https://api.github.com/users/jessicawoolard/repos