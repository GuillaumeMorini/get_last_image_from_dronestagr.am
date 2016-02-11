import urllib2
import json

URL="http://www.dronestagr.am/?json=1&count=1"
SIZE="full"
FILE="/Users/gmorini/Pictures/Wallpapers/dronestagr.am.jpg"

r = urllib2.Request(URL)
u = urllib2.urlopen(r)
j = json.load(u)
IMG_URL = j["posts"][0]["thumbnail_images"][SIZE]["url"]


import urllib
urllib.urlretrieve (IMG_URL, FILE)