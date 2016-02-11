import urllib2
import urllib
import json
import os

URL="http://www.dronestagr.am/?json=1&count=10"
SIZE="full"
FOLDER="/Users/gmorini/Pictures/Wallpapers/dronestagr.am/"

r = urllib2.Request(URL)
u = urllib2.urlopen(r)
j = json.load(u)

print "Len: "+str(len(j["posts"]))
print "Count: "+str(j["count"])
for i in j["posts"]:
    IMG_URL = i["thumbnail_images"][SIZE]["url"]
    print IMG_URL
    urllib.urlretrieve (IMG_URL, FOLDER+os.path.basename(IMG_URL))

