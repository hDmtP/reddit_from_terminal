# reddit_from_terminal

<br>

***stream comments, submissions from subreddits and users across `reddit` right in your terminal***

_Alert!_ : ~~Can't watch media contents(photos, videos, GIFs) in ur terminal.~~ *Its more developer centric so u get the `id` of every submission & post. You can google the `id` for watching the media content. Ex- imagine the `id` is `hrpzrt`. Then u will search in quote like this `"hrpzrt"` in the search bar*

<br>

## Requirements:
> Python3

<br>

## Installation:
open your terminal, select the directory u want this repo to be installed then paste the following commands:
```
git clone https://github.com/hDmtP/reddit_from_terminal
cd reddit_from_terminal
pip install -r requirements.txt
```
- **You need to have a reddit account**
  - Go to [this](https://www.reddit.com/prefs/apps) link.
  - scroll to the bottom and click `create app`
    - select `web app`
    - give `name`, `description` of ur choice
    - u can find ur `id` & `secret` there.
- **Create a new file `.env` in the same directory u installed this repo**
- Then write ur `id`, `secret` as following
```
id = "xxxxxxx"
secret = "xxxxxxx"
```
- Replace the `xxxxxxx` with ur id & secret
- Save the file and u r all set.

<br>

## How to run:
> python3 display.py

*Or u can make the `display.py` file executable by the following commands:*
```
cd reddit_from_terminal
chmod +x display.py
./display.py
```

You can update the repo with the following command(in case I update this repo in future)
>git pull

<br>

## Feedback
***If u have any idea to make this repo better u r most welcome to create any pull request :)***
