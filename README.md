#jenkins clean workspace script
clean slave's workspace which is deleted  


##workflow
1. Get all job list from jenkins api
2. Check local slave workspace's folder name,if it's not in job list,delete workspace
3. check All slave/node


#Jenkins job
##Clean workspace jenkins build shell
<http://qaci.intra.douban.com/job/clean_jenkins_workspace/>

```
hostname
rm -rf /data/jenkins/workspace/pylint.out
python clean_jenkins_workspace.py

#磁盘空间紧急的时候(<2G)清除/data/jenkins/workspace 30分钟之前的目录
sh cleanjenkinsworkspace.sh
```

##Jenkins trigger
<http://qaci.intra.douban.com/job/clean_jenkins_workspace_trigger/>

```
curl --silent --show-error --data 'json={"parameter":[{"name":"node","value":["YOURNODE1","YOURNODE2"]}]}&Submit=Build' http://qaci.intra.douban.com/job/clean_jenkins_workspace/build?token=YOURTOKEN
```


##Jenkins plugin


* <http://wiki.jenkins-ci.org/display/JENKINS/Parameterized+Build>
* <https://wiki.jenkins-ci.org/display/JENKINS/NodeLabel+Parameter+Plugin>