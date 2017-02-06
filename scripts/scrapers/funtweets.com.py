# funtweets.com.py
# Scrapes all tweets from http://funtweets.com/ and save them to csv file
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

from bs4 import BeautifulSoup as bs
import re
import unicodedata
import urllib
import csv

filepath = '../../data/funtweets.csv'
f = open(filepath, 'w')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )
totaljokes = 0
prefix = 'http://funtweets.com/'

for i in xrange(3088):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    tweets = html.find_all('div', {'class': 'tweet-text'})
    for tw in tweets:
        joke = tw.get_text()
        username = tw.find('a').get_text()
        joke = re.sub(username, '', joke)
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

f.close()
