from FileWrapper import FileWrapper
from bot import Bot

for i in range(1, 6):
    file_wrapper: FileWrapper = FileWrapper(filename="replied_posts.txt")
    bot: Bot = Bot(subreddit_name="toundrabotplayground", bot_name="bot1", file=file_wrapper)
    for comment in bot.find_comments_by_content(contains="\[reverse\]"):
        print("Replied to " + comment.id)
        comment.body = comment.body[9:]
        comment.reply(comment.body[::-1])
exit("program terminated safely")

