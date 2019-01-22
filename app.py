

from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():

    response = requests.get('https://api.github.com/users/jessicawoolard', headers=headers)
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

    response = requests.get('https://api.github.com/users/jessicawoolard', headers=headers)
    user = response.json()

    followers_response = requests.get(user['followers_url'])
    followers = followers_response.json()

    needed_followers = []
    for follower in followers:
        follower_dict = {
            'login': follower['login']
        }
        current_follower_responce = requests.get(follower['url'])
        current_follower = current_follower_responce.json()

        follower_dict['avatar_url'] = current_follower['avatar_url']
        follower_dict['name'] = current_follower['name']
        follower_dict['location'] = current_follower['location']
        follower_dict['bio'] = current_follower['bio']
        follower_dict['company'] = current_follower['company']

        needed_followers.append(follower_dict)

    context = {
        'profile': user,
        'followers': needed_followers
    }


    return render_template('followers.html', **context)