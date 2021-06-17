#!/bin/bash
#Simple script writen by AnnoX4uk. Useful for check active connections for some application
#See README.md for more information or run script without any options. 

#check whois
if [[ -z "$(which whois)" ]]; then
    echo "Whois package not installed. Please install whois and try again"
    exit
fi

#check netstat
if [[ -z "$(which netstat)" ]]; then
    echo "Netstat package not installed. Please install netstat and try again"
    exit
fi

#check privileges before starting
if (($EUID != 0)) ; then
    echo "Script running without root privileges"
    echo "If you want to see all connection set sudo before run"
fi


#set variables
programm_name=''
variable_connections=(TIME_WAIT ESTABLISHED CLOSE_WAIT LISTEN)
connection='ESTABLISHED'
out_lines=5
debug='OFF'

print_usage () {
    echo "Usage: netstat_scr -p {programm_name}"
    echo "Optional args:"
    echo "-l {LineNumbers} : number of output lines. By default output 5 lines"
    echo "-a : output all connection states. By default output ESTABLISHED only connections"
    echo "-d : debugging output"
    echo "-c : write connection type like TIME_WAIT or ESTABLISHED or CLOSE_WAIT or LISTEN"
}

#check arguments before start
if [ $# -lt 1 ]
then
echo "No valid options found."
print_usage
exit 1
fi

#parse arguments
while getopts "c:p:l:ad" opt
do
case $opt in
p) programm_name=$OPTARG
;;
a) connection='ALL' 
;;
c)  if [[ " ${variable_connections[*]} " != *" $OPTARG "*  ]]; then
        echo "Rescieve incorrect connection type, try again"
        exit 1
    elif [[ -z "$OPTARG" ]]; then
        echo "Rescive no special connection states after -c, work with ESTABLISHED connections"
    else 
        connection=$OPTARG
    fi
;;
d) debug='ON' 
;;
l) if [[ "$OPTARG" =~ [^0-9]+ ]]; then
  echo "Incorrent line numbers in -l option. Output $out_lines lines only"
   else 
   out_lines=$OPTARG
fi

;;
*) echo "Found invalid option!"
print_usage;;
esac
done

if [[ "$debug" == "ON" ]]; then
    echo "Program: $programm_name\
    connection: $connection\
    out lines: $out_lines"
    sleep 5s
    
fi


#check programm name for netstat
if [[ $programm_name == '-a' ]] | [[ $programm_name == '-l' ]]; then
    echo "Not found programm name."
    print_usage
    exit 1
fi

#check netstat connections 
if (( $connection == "ALL" )); then
    ip="$(netstat -tunapl)"
else
    ip="$(netstat -tunapl| grep "$connection")"
fi

if [[ "$debug" == "ON" ]]; then
    echo "Netstat output:\
    $ip"
    sleep 5s
fi


#check app connections
ip=$(echo "$ip" | awk '/'"$programm_name"/' {print $5}')

if [[ "$debug" == "ON" ]]; then
    echo "Netstat app output:\
    $ip"
    sleep 5s
fi

#Exit if blank output
if [ -z "$ip" ]; then
     echo "Not found connections for $programm_name"
     exit 1
fi

#convert netstat output to simple IP-addresses
ip=$(echo "$ip" |cut -d: -f1 | sort | uniq -c | sort | tail -n"$out_lines" | grep -oP '(\d+\.){3}\d+')

if [[ "$debug" == "ON" ]]; then
    echo "Address after convert:\
    $ip"
    sleep 5s
fi

#output organzation
for addr in $ip; do
    if [[ "$debug" == "ON" ]]; then
        echo "Try do whois to : $addr"
        sleep 5s
    fi
    org=$(whois "$addr")
    if [[ "$debug" == "ON" ]]; then
      echo "whois output:\
        $org"
        sleep 5s
    fi
    echo "$org" | awk -F':' '/^Organization/ {print $2}'
done
