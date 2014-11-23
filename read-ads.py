#!/usr/bin/python

import urllib2
import sys
import json
import pprint


pprint.pprint(sys.argv)

deviceId=sys.argv[1]
outputDir=(sys.argv[2])+"/"

print "Device ID: " + deviceId
print "dir: " + outputDir

url = "http://ad-line.biz/json/getAds?device_id="+deviceId
#print url
text=urllib2.urlopen(url).read(1000)
print "JSON received:"
print text
data=json.loads(text)
for item in data:
    filename=outputDir + item["ad_id"].zfill(6)+".txt";
    print(filename+": "+item["ad"])
    f = open(filename, "w");
    f.write(item["ad"])
    f.close()






