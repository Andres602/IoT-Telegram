#!/bin/sh

ps auxw | grep ./bot.py | grep -v grep > /dev/null

if [ $? != 0 ]
then
	screen -S bot -X stuff  '~/IoT-Telegram/bot/bot.py'$(echo '\015')
fi


ps auxw | grep ./server.py | grep -v grep > /dev/null

if [ $? != 0 ]
then
        screen -S server -X stuff  '~/IoT-Telegram/server/server.py 1025'$(echo '\015')
fi



ps auxw | grep redis-server | grep -v grep > /dev/null

if [ $? != 0 ]
then
        screen -S redis -X stuff  'redis-server'$(echo '\015')
fi
