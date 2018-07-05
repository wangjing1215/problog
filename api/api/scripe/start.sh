#!/bin/bash
isnull=`python /Users/yons/newwork/vala/minework/api/check.py $1`
if [ $isnull == 0 ]
then
echo 'please input like kp 8000'
exit
fi
a=`lsof -i:$1|grep python`
python /Users/yons/newwork/vala/sforid.py $a
a=`lsof -i:$1|grep python`
if [ $a=='' ]
then
echo 'the process has closed'
fi

