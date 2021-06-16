#!/bin/bash

#check privileges before starting
if (($EUID != 0)) ; then
    echo "Script running without root privileges"
    echo "If you want to see all connection set sudo before run"
fi

#set variables
programm_name=''
connection='ESTABLISHED'
out_lines=5

print_usage () {
    echo "Usage: netstat_scr -p {programm_name}"
    echo "Optional args:"
    echo "-l {LineNumbers} : number of output lines. By default output 5 lines"
    echo "-a : output all connection states. By default output ESTABLISHED only connections"
}

#check arguments before start
if [ $# -lt 1 ]
then
echo "No valid options found."
print_usage
exit 1
fi

#parse arguments
while getopts "p:l:a" opt
do
case $opt in
p) programm_name=$OPTARG
;;
a) connection='ALL' 
;;
l) out_lines=$OPTARG
;;
*) echo "Found invalid option!"
print_usage;;
esac
done

#check programm name for netstat
if [[ $programm_name == '-a' ]] | [[ $programm_name == '-l' ]]; then
    echo "Not found programm name."
    print_usage
    exit 1
fi


#netstat -tunapl | awk '/firefox/ {print $5}' | cut -d: -f1 | sort | uniq -c | sort | tail -n5 | grep -oP '(\d+\.){3}\d+' | while read IP ; do whois $IP | awk -F':' '/^Organization/ {print $2}' ; done
