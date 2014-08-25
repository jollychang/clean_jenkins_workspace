cleanjenkinsworkspace:
	df -h
	hostname
	rm -rf /data/jenkins/workspace/pylint.out
	python clean_jenkins_workspace.py

	#磁盘空间紧急的时候(<2G)清除/data/jenkins/workspace 30分钟之前的目录
	sh cleanjenkinsworkspace.sh
	df -h