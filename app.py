from flask import Flask, render_template, redirect, url_for,request
from flask import make_response

from login import login, login_with_access_token
from add_new_user import add_new_user
from add_new_comment import add_new_comment
from add_new_post import add_new_post
from fetch_comment_by_post_id import fetch_latest_comment
from fetch_latest_post import fetch_latest_post
from upvote_post_comment import update_vote_comment, update_vote_post

print(__name__)
app = Flask(__name__)

@app.route("/")
def home():
    return "hi"
@app.route("/index")

@app.route('/login', methods=['POST'])
def Login():
   message = None
   if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        result = login(username, password)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/login_with_new_access_token', methods=['POST'])
def LoginWithAccessToken():
   message = None
   if request.method == 'POST':
        user_id = request.json['user_id']
        access_token = request.json['access_token']
        result = login_with_access_token(user_id, access_token)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/signup', methods=['POST'])
def Signup():
   message = None
   if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        result = add_new_user(username, password, first_name, last_name)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/post_new_comment', methods=['POST'])
def AddNewComment():
   message = None
   if request.method == 'POST':
        user_id = request.json['user_id']
        post_id = request.json['post_id']
        content = request.json['content']
        result = add_new_comment(user_id, post_id, content)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/post_new_post', methods=['POST'])
def AddNewPost():
   message = None
   if request.method == 'POST':
        user_id = request.json['user_id']
        title = request.json['title']
        content = request.json['content']
        result = add_new_post(user_id, title, content)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/fetch_comment', methods=['POST'])
def FetchLatestComment():
   message = None
   if request.method == 'POST':
        post_id = request.json['post_id']
        first_n_comment = request.json['first_n_comment']
        num_of_comments = request.json['num_of_comments']
        result = fetch_latest_comment(post_id, first_n_comment, num_of_comments)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/fetch_latest_post', methods=['POST'])
def FetchLatestPost():
   message = None
   if request.method == 'POST':
        first_n_post = request.json['first_n_post']
        num_of_posts = request.json['num_of_posts']
        result = fetch_latest_post(first_n_post, num_of_posts)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/upvote_post', methods=['POST'])
def UpvotePost():
   message = None
   if request.method == 'POST':
        post_id = request.json['post_id']
        result = update_vote_post(post_id)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

@app.route('/upvote_comment', methods=['POST'])
def UpvoteComment():
   message = None
   if request.method == 'POST':
        comment_id = request.json['comment_id']
        result = update_vote_comment(comment_id)
        print(result)
        resp = make_response(result)
        resp.headers['Content-Type'] = "application/json"
        return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')