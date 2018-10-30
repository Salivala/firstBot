import re
import praw
import praw.models
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

    def find_comments_by_content(self, contains: str) -> list:
        matched_comments = []
        for submission in self.subreddit.hot(limit=2000):
            submission.comments.replace_more()
            for comment in submission.comments.list():
                if comment.id not in self.file.posts:
                    txt = comment.body
                    match = re.search(contains, txt)
                    if match:
                        self.file.posts.append(comment.id)
                        matched_comments.append(comment)
        self.file.write_file()
        return matched_comments
