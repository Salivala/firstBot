import sys
import re
import praw
import typing
from FileWrapper import FileWrapper


class Bot:
    def __init__(self, subreddit_name, bot_name, file : FileWrapper):
        self.subreddit_name = subreddit_name
        self.bot_name = bot_name
        self.reddit = self.__fetch_reddit()
        self.subreddit = self.reddit.subreddit(subreddit_name)
        self.file = file

    def __fetch_reddit(self):
        return praw.Reddit(self.bot_name)

    def find_comment_by_content(self, contains):
        for submission in self.subreddit.hot(limit=20):
            if submission.id not in self.file.posts:
                if re.search("testing", submission.title, re.IGNORECASE):
                    submission.reply("wow mate")
                    print("Bot replying")
                    self.file.posts.append(submission.id)
