import sys
import re
import praw

class bot:
    def __init__(self, subreddit_name, bot_name):
        self.subreddit_name = subreddit_name
        self.bot_name = bot_name

    def fetch_reddit(self):
        return praw.Reddit(self.bot_name)

    def find_comment_by_content(self, contains):
        return self.subreddit_name
