# json_to_csv.py
# Takes all json files of reddit posts, parses jokes from them 
# and writes into a single csv file
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

# extracts jokes from json file
import os
import json
import unicodedata
import csv

# reddit-jokes-jsondump can be downloaded from http://
# contains json files of reddit /r/jokes posts from 25 Jan 2008 to 31 Jan 2017
folder_path = '../reddit-jokes-jsondump/'
files = os.listdir(folder_path)
for i in xrange(len(files)):
    files[i] = folder_path + files[i]

# given json data, return joke
def get_joke(data):
    title = data[0]['data']['children'][0]['data']['title']
    selftext = data[0]['data']['children'][0]['data']['selftext']
    if len(selftext) < len(title):
        return title + " " + selftext
    n = len(title)
    # if title is repeated in post text, ignore it
    if (selftext[:n] == title):
        return selftext
    # else return title + selftext as joke
    return title + " " + selftext

# write all jokes to csv file
f = open('../data/reddit-jokes.csv', 'w')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )
idx = 0
total_jokes = len(files)
for filepath in files: 
    data_file = open(filepath)
    data = json.load(data_file)
    joke = get_joke(data)
    joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
    joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...")
    joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
    idx += 1
    writer.writerow((idx, joke)) 
    data_file.close()
    print ("%d / %d jokes processed" % (idx, total_jokes))
f.close()
