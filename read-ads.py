import urllib2
import json
import pprint

deviceId="32"
url = "http://ad-line.biz/json/getAds?device_id="+deviceId
#print url
text=urllib2.urlopen(url).read(1000)
print "JSON received:"
print text
data=json.loads(text)
for item in data:
    filename=item["ad_id"]+".txt";
    print(filename+": "+item["ad"])
    f = open(filename, "w");
    f.write(item["ad"])
    f.close()






