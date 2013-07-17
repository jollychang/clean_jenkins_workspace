function cleanjenkinsworkspace() {
    find /data/jenkins/workspace -mindepth 1 -maxdepth 1 -mmin +30 -print -type d | xargs rm -rf

}

diskfree=`df |grep data | awk '{print $4}'`
if [[ $diskfree -lt 2000000 ]]; then
    echo "less then 2G, clean workspace"
    cleanjenkinsworkspace
fi
