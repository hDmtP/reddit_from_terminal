import praw
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def authenticate():
    reddit = praw.Reddit(
        client_id=os.environ.get("id"),
        client_secret=os.environ.get("secret"),
        user_agent='random bullshit go brrr..',
    )
    return reddit


reddit = authenticate()

if reddit.read_only:
    print("\n\n\t\t=======================================\t\t\t")
    print("\t\t|| All set, ready to explore Reddit! ||\t\t\t")
    print("\t\t=======================================\t\t\t")


def sub_comment_stream():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    for comment in subreddit.stream.comments(skip_existing=True, pause_after=5):
        print("\n\n\n")
        print(f"user:{comment.author}\nid:{comment}\ncomment:{comment.body}")


def sub_submission_stream():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.stream.submissions(skip_existing=True, pause_after=5):
        print("\n\n\n")
        print(
            f"user:{submission.author}\nid:{submission}\ntitle:{submission.title}\n\n")
        print(f"Link:https://www.reddit.com/r/{sub}/comments/{submission}/")


def sub_submissions_hot():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    limit = int(input("Limit: "))
    for submission in subreddit.hot(limit=limit):
        print("\n\n\n")
        print(
            f"user:{submission.author}\nid:{submission}\ntitle:{submission.title}\n\n")
        print(f"Link:https://www.reddit.com/r/{sub}/comments/{submission}/")


def redditor_stream_comnts():
    user = str(input("reddit username: "))
    for comment in reddit.redditor(user).stream.comments():
        print("\n\n\n")
        print(f"id:{comment}\ncomment:{comment.body}")


def redditor_stream_submissions():
    user = str(input("reddit username: "))
    for submission in reddit.redditor(user).stream.submissions():
        print("\n\n\n")
        print(f"id:{submission}\ntitle:{submission.title}")


def sub_submissions_top():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    limit = int(input("Limit: "))
    for submission in subreddit.top(limit=limit):
        print("\n\n\n")
        print(
        f"user:{submission.author}\nid:{submission}\ntitle:{submission.title}\n\n")
        print(f"Link:https://www.reddit.com/r/{sub}/comments/{submission}/")


def search_sub():
    keyword = str(input("Enter keyword for search: "))
    sub = str(input("Enter subreddit name: "))
    i = 0
    import re

    def findWholeWord(w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot():
        if findWholeWord(keyword)(str(submission.title)) != None:
            i = i+1
            print(f"Link:https://www.reddit.com/r/{sub}/comments/{submission}/\n\n")
            print(f"total items found till....: {i}\n\n")

    for submission in subreddit.new():
        if findWholeWord(keyword)(str(submission.title)) != None:
            i = i+1
            print(f"Link:https://www.reddit.com/r/{sub}/comments/{submission}/\n\n")
            print(f"total items found till....: {i}\n\n")

    for submission in subreddit.top():
        if findWholeWord(keyword)(str(submission.title)) != None:
            i = i+1
            print(f"Link:https://www.reddit.com/r/{sub}/comments/{submission}/\n\n")
            print(f"total items found till....: {i}\n\n")
