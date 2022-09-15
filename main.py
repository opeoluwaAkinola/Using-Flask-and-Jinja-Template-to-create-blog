# import flask and post module
from flask import Flask, render_template
from post import Post

# create blog object from Post() class
blogs=Post()

# open Flask class with name of this script
app = Flask(__name__)

# initialize route decorator with for function "home()" to return the home page and the posts
# to be used by the jinja template in the home page
@app.route('/')
def home():
    # get blogs with
    posts=blogs.posts
    return render_template("index.html",blogs=posts)

# initialize the route decorator but with specified url with the id of the posts.
# the decorator wraps the get_blog() function which returns the pages showing
# the posts and takes in the specified post from the Post.get_post() function
@app.route('/post/<num>')
def get_blog(num):
    print(num)
    post=blogs.get_posts(num)
    print(post)
    return render_template("post.html",blog=post)

if __name__ == "__main__":
    app.run(debug=True)
