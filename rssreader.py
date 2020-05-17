import feedparser
import datetime
from datetime import datetime as dt
import time
import re

class Postman():
    def __init__(self):
        self.ns = feedparser.parse("http://www.horriblesubs.info/rss.php?res=1080")
        self.newestDate = dt(2020, 5, 17, 0, 0, 0 , 7, datetime.timezone.utc)

    def refresh(self):
        self.ns = feedparser.parse("http://www.horriblesubs.info/rss.php?res=1080")

    def postsToday(self):
        self.refresh()
        posts = []
        for entry in self.ns.entries:
            date = dt.strptime(entry.published, "%a, %d %B %Y %H:%M:%S %z")
            if self.newestDate < date:
                posts.append(entry)
            else:
                if len(posts) > 0:
                    self.newestDate = dt.strptime(posts[0].published, "%a, %d %B %Y %H:%M:%S %z")
                break
        print("end fetch")
        return posts
    def getPosts(self):
        posts = self.postsToday()
        titles = "New releases: \n"
        if len(posts) == 0:
            return "nothing"
        for post in posts:
            st = re.sub('^\[.*\] ', '', post.title)
            st = re.sub(' \[.*\].mkv$', '', st)
            titles += (st+"\n")
        return titles