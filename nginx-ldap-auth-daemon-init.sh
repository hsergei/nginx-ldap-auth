#!/bin/sh

CMD=/usr/bin/nginx-ldap-auth-daemon

PIDFILE=/var/run/nginx-ldap-auth-daemon.pid

. /etc/init.d/functions

start() {
    echo -n "Starting ldap-auth-daemon: "
    if [ -s ${PIDFILE} ]; then
       RETVAL=1
       echo -n "Already running !" && warning
       echo
    else
       nohup ${CMD} >/dev/null 2>&1 &
       RETVAL=$?
       PID=$!
       [ $RETVAL -eq 0 ] && success || failure
       echo
       echo $PID > ${PIDFILE}
    fi
}

case $1 in
    "start")
        start
    ;;
    "stop")
        echo -n "Stopping nginx-ldap-auth-daemon: "
        killproc -p $PIDFILE $CMD
        echo
    ;;
    *)
        echo "Usage: $0 <start|stop>"
    ;;
esac
