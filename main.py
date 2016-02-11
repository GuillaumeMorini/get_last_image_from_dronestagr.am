import urllib2
import urllib
import json
import os

URL="http://www.dronestagr.am/?json=1&count=1"
SIZE="full"
FOLDER="/Users/gmorini/Pictures/Wallpapers/dronestagr.am/"

r = urllib2.Request(URL)
u = urllib2.urlopen(r)
j = json.load(u)
IMG_URL = j["posts"][0]["thumbnail_images"][SIZE]["url"]


urllib.urlretrieve (IMG_URL, FOLDER+os.path.basename(IMG_URL))

