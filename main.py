import sys
import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

if not os.path.isfile("replied_posts.txt"):
    replied_posts = []
else:
    with open("replied_posts.txt", "r") as f:
        replied_posts = f.read()
        replied_posts = replied_posts.split("\n")
        replied_posts = list(filter(None, replied_posts))

subreddit = reddit.subreddit("toundrabotplayground")

for submission in subreddit.hot(limit=10):
    #print(submission.id)
    if submission.id not in replied_posts:
        if re.search("testing", submission.title, re.IGNORECASE):
            submission.reply("wow good job dude!")
            print("Boy replying to : ", submission.title)
            replied_posts.append(submission.id)


with open("replied_posts.txt", "w") as f:
    for post_id in replied_posts:
        f.write(post_id + "\n")
