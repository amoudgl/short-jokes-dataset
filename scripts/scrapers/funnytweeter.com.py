# funnytweeter.com.py
# Scrapes all tweets from http://funnytweeter.com/ and save them to csv file
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

import requests
from bs4 import BeautifulSoup as bs
import unicodedata
import csv

filepath = '../../data/funnytweeter.csv'
f = open(filepath, 'w')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )
totaljokes = 0
prefix = 'http://funnytweeter.com/page/'

for i in xrange(4580):
    url = prefix + str(i + 1) + '/'
    r = requests.get(url).text
    html = bs(r, 'html.parser')
    jokes = html.find_all('div', {'class': 'article_wrap'})
    for joke in jokes:
        # save only text tweets, ignore the ones with image
        if (joke.find_all('img', {'class': 'tweet_media'})[0]['src'] == ''):
            joke = joke.find_all('p')[0].get_text().split(":", 1)[1]
            joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
            joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
            joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
            totaljokes += 1
            writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

f.close()
