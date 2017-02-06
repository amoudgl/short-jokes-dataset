# subredditarchive.py
# Modified version of https://github.com/peoplma/subredditarchive to work with the latest praw API
# Saves all posts of a subreddit in json format between given timestamps
#
# Copyright (C) 2017  Abhinav Moudgil
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import time
import datetime
import praw
import os
import traceback
import requests
import json
b = "timestamp:"
d = ".."

# enter your config details here
# for more info, visit https://github.com/reddit/reddit/wiki/OAuth2
r = praw.Reddit(     client_id= '',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')
def resume():
	if os.path.exists('config.txt'):
		line = file('config.txt').read()
		startStamp,endStamp,step,subName=line.split(',')
		startStamp,endStamp,step=int(startStamp),int(endStamp),int(step)
		return startStamp,endStamp,step,subName
	else:
		return 0
choice = input('\nMENU\nPlease choose one of the following:\n1. Start New Archive\n2. Continue Archiving\n3. Exit\n(Input the number)\n')
if(choice==1):
	subName=raw_input('Input the subreddit to archive: ')
	sdate=raw_input('Input start date in the format dd/mm/yyyy: ')
	startStamp= int(time.mktime(datetime.datetime.strptime(sdate, "%d/%m/%Y").timetuple()))
	edate=raw_input('Input end date in the format dd/mm/yyyy: ')
	endStamp= int(time.mktime(datetime.datetime.strptime(edate, "%d/%m/%Y").timetuple()))
	step=input('Input seconds between each search, 30 recommended: ')
	obj=file('config.txt','w')
	obj.write(str(startStamp)+','+str(endStamp)+','+str(step)+','+str(subName))
	obj.close()
elif(choice==2):
	try:
		startStamp,endStamp,step,subName=resume()
	except:
		print('Nothing to continue.')
		exit()
else:
	exit()	
sdate=datetime.datetime.fromtimestamp(int(startStamp)).strftime('%d-%m-%Y')
edate=datetime.datetime.fromtimestamp(int(endStamp)).strftime('%d-%m-%Y')
folderName=str(subName+' '+str(sdate)+' '+str(edate))
if not os.path.exists(folderName):
    os.makedirs(folderName)
    
def getNew(subName,folderName):
    subreddit_comment = r.get_comments(subName, limit=1000)
    subreddit_posts = r.get_submissions(subName, limit=1000)
    for comment in subreddit_comment:
        print comment
        url= "https://www.reddit.com" + comment.permalink
        data= {'user-agent':'archive by /u/healdb'}
        response = requests.get(url+'.json',headers=data)
        filename=folderName+"/"+comment.name
        obj=open(filename, 'w')
        obj.write(response.text)
        obj.close()
    for post in subreddit_posts:
        print post
        url1= "https://www.reddit.com" + post.permalink
        data= {'user-agent':'archive by /u/healdb'}
        if submission.id not in already_done:
            response = requests.get(url1+'.json',headers=data)
            filename=folderName+"/"+post.name
            obj=open(filename, 'w')
            obj.write(response.text)
            obj.close()
            already_done.add(submission.id)
        else:
            continue
def main(startStamp,endStamp,step,folderName,subName,progress):
    count=step
    try:
        startStamp =open(folderName+"/lastTimestamp.txt").read()
        print("Resuming from timestamp: " + startStamp)
        time.sleep(3)
        startStamp=int(startStamp)
        progress=startStamp
    except: 
        pass
    c=1
    for currentStamp in range(startStamp,endStamp,step):
        e=' --'
        if(c%2==0):
            e=' |'
        f = str(currentStamp)
        g = str(currentStamp+step)
        search_results = r.subreddit(subName).search(b+f+d+g, syntax='cloudsearch')
        end=str((int((float(count)/float(progress)*20.0))*10)/2)+'%'
        count+=step
        for post in search_results:
            print("---I found a post! It\'s called:" + str(post))
            url= (post.permalink).replace('?ref=search_posts','')
            url = "https://www.reddit.com" + url
            data= {'user-agent':'archive by /u/healdb'}
            response = requests.get(url+'.json',headers=data)
            filename=folderName+"/"+post.name+'.json'
            obj=open(filename, 'w')
            obj.write(response.text)
            obj.close()
            time.sleep(1)
        obj=open(folderName+"/lastTimestamp.txt", 'w')
        obj.write(str(currentStamp))
        obj.close()
        c+=1
    print('Welp, all done here! Stopped at timestamp '+ str(currentStamp))
progress = endStamp-startStamp
while True:
    try:
        main(startStamp,endStamp,step,folderName,subName,progress)
        print("Succesfully got all posts within parameters.")
        choice=input('You can now either\n1. Exit\n2. Get new posts\n(Input the number)\n')
        if(choice==1):
            exit()
        else:
            while True:
                getNew(subName,folderName)
    except KeyboardInterrupt:
        exit()
    except SystemExit:
        exit()
    except:
        print("Error in the program! The error was as follows: ")
        error = traceback.format_exc()
        time.sleep(5)
        print(error)
        time.sleep(5)
        print("Resuming in 5 seconds...")
        time.sleep(5)
