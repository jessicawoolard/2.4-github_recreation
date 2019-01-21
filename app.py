

from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():

    response = requests.get('https://api.github.com/users/jessicawoolard')
    user = response.json()

    repos_response = requests.get(user['repos_url'])
    repos = repos_response.json()

    # print(repos)

    context = {
        'profile': user,
        'repos': repos
    }


    return render_template('index.html', **context)




@app.route('/followers')
def followers():

    response = requests.get('https://api.github.com/users/jessicawoolard')
    user = response.json()

    followers_response = requests.get(user['followers_url'])
    followers = followers_response.json()


    context = {
        'profile': user,
        'followers': followers
    }


    return render_template('followers.html', **context)