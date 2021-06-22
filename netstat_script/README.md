## Small script for netstat output

Use this netstat_scr.sh to output your connection states

### Prepare installation

Before use this script you must have whois and netstat utility

### Installation

Download netstat_scr.sh to your system with your favorite way (git/browser/wget/copy-paste)

Check privileges on script 

 `ls -lA ./netstat_scr.sh`
For usage you need check x flag like this: 
 
 `-rwxr-xr-x@ 1 username  usergroup  4591 Jun 17 19:48 ./netstat_scr.sh`

If you have not x permissions, use chmod utility.

### USAGE

 `./netstat_scr.sh -p {PROCESS_NAME}`

By default work in user privileges, optional you can run it with sudo.

 `sudo ./netstat_scr.sh -p {PROCESS_NAME}`

You can set lines to output with -l. By default output is 5 lines.

 `./netstat_scr.sh -p {PROCESS_NAME} -l 100`

By default, output only ESTABLISHED states. You can use -a option to see all output

 `./netstat_scr.sh -p {PROCESS_NAME} -a`

For userfriendly output set -u option

 `./netstat_scr.sh -p {PROCESS_NAME} -u`

For search by connection type (like TIME_WAIT or ESTABLISHED or CLOSE_WAIT or LISTEN) use -c option:

 `./netstat_scr.sh -p {PROCESS_NAME} -c LISTEN`

By default script return Organization cell from whois request. For output another information, use -i option:

 `./netstat_scr.sh -p {PROCESS_NAME} -i origin`

### Example

 `./netstat_scr.sh -p nginx -u -i origin -l 100`

