#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib, json , os

url = 'http://qaci.intra.douban.com/api/python?pretty=true'

data =  eval(urllib.urlopen(url).read())
jobnames = []
for job in data['jobs']:
    jobnames.append(job['name'])


ws = os.listdir('/data/jenkins/workspace/')

for workspace in ws:
    if workspace not in jobnames:
        print workspace