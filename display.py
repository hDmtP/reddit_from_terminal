from reddit_dose import *
import fontstyle


def choose():
    choice = int(input(fontstyle.apply("\n\n\n0 -> sub_comment_stream \n\n 1 -> sub_submissions_hot \n\n 2 -> sub_submission_stream \n\n 3 -> redditor_stream_comnts \n\n 4 -> redditor_stream_submissions \n\n 5 -> sub_submissions_top \n\n 6 -> search \n\n 7 -> close(): ", "bold/Italic/purple")))
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

choose()
