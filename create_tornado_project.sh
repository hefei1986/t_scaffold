#!/usr/bin/bash
#! -*- coding: utf-8 -*-
#! author: hefei1986@gmail.com



help()
{
    echo "HELP"
    echo "usage: create a void tornado project:"
    echo "    bash create_tornado_project.sh PROJECT_NAME"
    echo ""
    echo "exmaple:"
    echo "    bash create_tornado_project.sh hello_world"
    echo ""
}

# main begin

if [ $# -lt 1 ];then
    help
    exit 0
fi

if [ $# -gt 1 ]; then
    help
    exit 0
fi

echo $1

if [ ! -d tpl ]; then
    echo "directory tpl not found"
fi

if [ -d $1 ]; then
    echo "directory $1 existed"
fi

cp -r ./tpl "./$1"

sed -i "s/\$MODULE_NAME/${1}_/g" "./$1/config/settings.py"
