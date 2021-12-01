from reddit_dose import *


def choose():
    choice = int(input("0 -> sub_comment_stream | 1 -> sub_submissions_hot | 2 -> sub_submission_stream | 3 -> redditor_stream_comnts | 4 -> redditor_stream_submissions: "))
    if(choice == 0):
        try:
            sub_comment_stream()
        except KeyboardInterrupt:
            print("\n\tAdios!\n\t")
    elif(choice == 1):
        try:
            sub_submissions_hot()
        except KeyboardInterrupt:
            print("\n\tAdios!\n\t")
    elif(choice == 2):
        try:
            sub_submission_stream()
        except KeyboardInterrupt:
            print("\n\tAdios!\n\t")
    elif(choice == 3):
        try:
            redditor_stream_comnts()
        except KeyboardInterrupt:
            print("\n\tAdios!\n\t")
    elif(choice == 4):
        try:
            redditor_stream_submissions()
        except KeyboardInterrupt:
            print("\n\tAdios!\n\t")

choose()