#jenkins clean workspace script
clean slave's workspace which is deleted  
<http://qaci.intra.douban.com/job/clean_jenkins_workspace/>


##workflow
1. Get all job list from jenkins api
2. Check local slave workspace's folder name,if it's not in job list,delete workspace
3. check All slave/node


##Jenkins plugin


* <http://wiki.jenkins-ci.org/display/JENKINS/Parameterized+Build>
* <https://wiki.jenkins-ci.org/display/JENKINS/NodeLabel+Parameter+Plugin>