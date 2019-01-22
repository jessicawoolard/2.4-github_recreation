
try:
    from github_key import github_api_token
    headers = {'Authorization': 'token {}'.format(github_api_token)}
except:
    print('Hey i see yu dont have a github API key.')
    print('No worries. we will just use the public API')
    headers = {}

from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():

    response = requests.get('https://api.github.com/users/jessicawoolard', headers=headers)

    user = response.json()

    repos_response = requests.get(user['repos_url'], headers=headers)
    repos = repos_response.json()
    print('response', repos)
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

    followers_response = requests.get(user['followers_url'], headers=headers)
    followers = followers_response.json()

    needed_followers = []
    for follower in followers:
        follower_dict = {
            'login': follower['login']
        }
        current_follower_response = requests.get(follower['url'], headers=headers)
        current_follower = current_follower_response.json()

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