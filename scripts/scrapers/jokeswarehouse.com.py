# jokeswarehouse.com.py
# Scrapes jokes from http://jokeswarehouse.com/ and and save them to csv file
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
import unicodedata
import urllib
import csv
import sys

filepath = '../../data/jokeswarehouse.csv'
f = open(filepath, 'w')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )

# extract urls
url = 'http://www.jokeswarehouse.com/cgi-bin/bydate.cgi'
r = urllib.urlopen(url).read()
html = bs(r, 'html.parser')
urls = html.find_all('a')
urls = [url['href'] for url in urls]
totaljokes = 0

for url in urls:
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    suburls = html.find_all('a')
    suburls = [suburl['href'] for suburl in suburls]
    for suburl in suburls:
        r = urllib.urlopen(suburl).read()
        html = bs(r, 'html.parser')
        joke = html.find('p').get_text()
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...")
        totaljokes += 1
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        writer.writerow((totaljokes, joke))
    print ("total number of jokes processed = %d" %(totaljokes))

f.close()
