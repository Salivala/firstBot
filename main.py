import sys
import praw
import pdb
import re
import os
from FileWrapper import FileWrapper
from bot import Bot

print("starting")
while True:
    file_wrapper: FileWrapper = FileWrapper(filename="replied_posts.txt")
    bot: Bot = Bot(subreddit_name="toundrabotplayground", bot_name="bot1", file=file_wrapper)
    for comment in bot.find_comments_by_content(contains="\[reverse\]"):
        print("wow!" + comment.id)
        comment.body = comment.body[9:]
        comment.reply(comment.body[::-1])

