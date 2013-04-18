#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib, json , os
from shutil import rmtree

url = 'http://qaci.intra.douban.com/api/python?pretty=true'
jenkins_workspace_path = '/data/jenkins/workspace/'

data =  eval(urllib.urlopen(url).read())
jobnames = []
for job in data['jobs']:
    jobnames.append(job['name'])


ws = os.listdir(jenkins_workspace_path)

for workspace in ws:
    if workspace not in jobnames:
    	workspace_path = os.path.join(jenkins_workspace_path, workspace)
        print "remove dir: %s " % workspace_path
        rmtree(workspace_path)