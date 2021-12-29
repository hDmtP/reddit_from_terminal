#!/usr/bin/python3
import praw
import fontstyle
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
    print("\n")
    print(fontstyle.apply("=======================================", "bold/red/YELLOW_BG"))
    print(fontstyle.apply("|| Aight!!, Ready to explore Reddit! ||", "bold/white/BLACK_BG"))
    print(fontstyle.apply("=======================================", "bold/red/YELLOW_BG"))


def sub_comment_stream():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    for comment in subreddit.stream.comments(skip_existing=True, pause_after=5):
        print("\n\n\n")
        print(fontstyle.apply(f"user:{comment.author}\nid:{comment}\ncomment:{comment.body}", "bold/green"))


def sub_submission_stream():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.stream.submissions(skip_existing=True, pause_after=5):
        print("\n\n\n")
        print(fontstyle.apply(
            f"user:{submission.author}\nid:{submission}\ntitle:{submission.title}\n\n", "bold/green"))
        print(fontstyle.apply(f"Link: https://www.reddit.com/r/{sub}/comments/{submission}/", "bold/Italic/cyan"))


def sub_submissions_hot():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    limit = int(input("Limit: "))
    for submission in subreddit.hot(limit=limit):
        print("\n\n\n")
        print(fontstyle.apply(
            f"user:{submission.author}\nid:{submission}\ntitle:{submission.title}\n\n", "bold/green"))
        print(fontstyle.apply(f"Link: https://www.reddit.com/r/{sub}/comments/{submission}/", "bold/Italic/cyan"))


def redditor_stream_comnts():
    user = str(input("reddit username: "))
    for comment in reddit.redditor(user).stream.comments():
        print("\n\n\n")
        print(fontstyle.apply(f"id:{comment}\ncomment:{comment.body}", "bold/cyan"))


def redditor_stream_submissions():
    user = str(input("reddit username: "))
    for submission in reddit.redditor(user).stream.submissions():
        print("\n\n\n")
        print(fontstyle.apply(f"id:{submission}\ntitle:{submission.title}", "bold/cyan"))


def sub_submissions_top():
    sub = str(input("Enter subreddit name: "))
    subreddit = reddit.subreddit(sub)
    limit = int(input("Limit: "))
    for submission in subreddit.top(limit=limit):
        print("\n\n\n")
        print(fontstyle.apply(
        f"user:{submission.author}\nid:{submission}\ntitle:{submission.title}\n\n", "bold/green"))
        print(fontstyle.apply(f"Link: https://www.reddit.com/r/{sub}/comments/{submission}/", "bold/Italic/cyan"))


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
            print(fontstyle.apply(f"Link: https://www.reddit.com/r/{sub}/comments/{submission}/\n\n", "bold/Italic/green"))
            print(fontstyle.apply(f"total items found till....: {i}\n\n", "Italic/yellow"))

    for submission in subreddit.new():
        if findWholeWord(keyword)(str(submission.title)) != None:
            i = i+1
            print(fontstyle.apply(f"Link: https://www.reddit.com/r/{sub}/comments/{submission}/\n\n", "bold/Italic/green"))
            print(fontstyle.apply(f"total items found till....: {i}\n\n", "Italic/yellow"))

    for submission in subreddit.top():
        if findWholeWord(keyword)(str(submission.title)) != None:
            i = i+1
            print(fontstyle.apply(f"Link: https://www.reddit.com/r/{sub}/comments/{submission}/\n\n", "bold/Italic/green"))
            print(fontstyle.apply(f"total items found till....: {i}\n\n", "Italic/yellow"))

            
def search_comment():
    keyword = str(input("Enter keyword for search: "))
    sub = str(input("Enter subreddit name: "))
    i = 0
    import re

    def findWholeWord(w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    subreddit = reddit.subreddit(sub)
    for comment in subreddit.stream.comments():
        if findWholeWord(keyword)(str(comment.body)) != None:
            i = i+1
            print(fontstyle.apply(f"\n\nuser:{comment.author}\nid:{comment}\ncomment:{comment.body}\n\n", "bold/darkcyan"))
            print(fontstyle.apply(f"total items found till....: {i}\n\n", "Italic/yellow"))


def search_user_comment():
    username = str(input("Enter username for search: "))
    sub = str(input("Enter subreddit name: "))
    i = 0

    subreddit = reddit.subreddit(sub)
    for comment in subreddit.stream.comments():
        if username == str(comment.author):
            i = i+1
            print(fontstyle.apply(f"\n\nuser:{comment.author}\nid:{comment}\ncomment:{comment.body}\n\n", "bold/darkcyan"))
            print(fontstyle.apply(f"total items found till....: {i}\n\n", "Italic/yellow"))

def choose():
    choice = int(input(fontstyle.apply("\n\n\n 0 -> sub_comment_stream \n\n 1 -> sub_submissions_hot \n\n 2 -> sub_submission_stream \n\n 3 -> redditor_stream_comnts \n\n 4 -> redditor_stream_submissions \n\n 5 -> sub_submissions_top \n\n 6 -> search subreddit \n\n 7 -> search comments \n\n 8 -> search an user's comment \n\n 9 -> exit(): ", "bold/Italic/purple")))
    
    if(choice == 0):
        try:
            sub_comment_stream()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 1):
        try:
            sub_submissions_hot()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 2):
        try:
            sub_submission_stream()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 3):
        try:
            redditor_stream_comnts()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 4):
        try:
            redditor_stream_submissions()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 5):
        try:
            sub_submissions_top()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 6):
        try:
            search_sub()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 7):
        try:
            search_comment()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 8):
        try:
            search_user_comment()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))

if __name__ == "__main__":
	choose()
