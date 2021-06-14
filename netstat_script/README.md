## Small script for netstat output

Use this netstat_scr.sh to output your connection states

###USAGE

'./netstat_scr.sh {PROCESS_NAME}'

By default work in user privileges, optional you can run it with sudo.

'sudo ./netstat_scr.sh {PROCESS_NAME}'

You can set lines to output with -l

'./netstat_scr.sh {PROCESS_NAME} -l 100'

By default, output only ESTABLISHED states. You can use -a option to see all output

'./netstat_scr.sh {PROCESS_NAME} -a'


