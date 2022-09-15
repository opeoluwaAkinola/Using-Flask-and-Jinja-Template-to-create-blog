# import request module to get json file for blog from the api
import requests
# Create post class
class Post:
    # initializing post class will get the blogs as a json file
    def __init__(self):
        self.posts =requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    # Function to get the blog title, subtitle and body with the title as a list in the order
    # [title, subtitle, body]
    def get_posts(self,id):
        # create empty list
        post=[]
        for post_ in self.posts:
            if post_["id"] == int(id):
                post.append(post_["title"])
                post.append(post_["subtitle"])
                post.append(post_["body"])
        return post