#!/bin/bash

# Gitlab Liveness OK response
OK_STATUS="{\"status\":\"ok\"}"

printhelp()
{
cat << EOF
usage: $1 [-h] -u URL [-t TIMEOUT] [-d]

GitLab liveness check

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           debug mode

required arguments:
  -u URL, --url URL     GitLab liveness URL to check
  -t TIMEOUT, --timeout TIMEOUT

EOF
}

# Temporary file to save possible error message(s)
ERRF=`mktemp`

OPTS=`getopt -o t:,h,u:,d -l timeout:,help,url:,--debug -- "$@" 2> $ERRF`
if [ $? != 0 ]
then
    cat $ERRF
    rm $ERRF
    exit 3
fi

rm $ERRF

eval set -- "$OPTS"

# default debug off
DEBUG=0

# how we were called
NAME=$0

while true ; do
    case "$1" in
        -t|--timeout) TIMEOUT=$2; shift 2;;
        -h|--help) printhelp $NAME; exit 3;;
        -u|--url) URL=$2; shift 2 ;;
        -d|--debug) DEBUG=1; shift ;;
        --) shift; break;;
    esac
done

if [ -z $TIMEOUT ]
then
   echo Please specify a timeout value
   exit 3
fi

if [ -z $URL ]
then
   echo Please specify a liveness URL
   exit 3
fi

[ $DEBUG == 1 ] && echo Liveness URL=$URL

# Temporary file to save response
RESPONSE=`mktemp`

ERRF=`mktemp`

[ $DEBUG == 1 ] && echo Connecting to liveness URL...

wget -nv -T $TIMEOUT -O $RESPONSE $URL 2> $ERRF

if [ $? != 0 ]
then
    cat $ERRF
    rm $ERRF
    rm $RESPONSE
    exit 2
fi

rm $ERRF

RES=`cat $RESPONSE`

[ $DEBUG == 1 ] && echo Server response was: "$RES"

RETVAL=0

# Compare server response to OK response
if [ "$RES" != "$OK_STATUS" ]
then
   RETVAL=1
fi

cat $RESPONSE

echo

rm $RESPONSE

exit $RETVAL
