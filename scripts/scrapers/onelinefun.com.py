# onelinefun.com.py
# Scrapes jokes from http://onelinefun.com/ and and save them to csv file
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

filepath = '../../data/onelinefun.csv'
f = open(filepath, 'w')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )
totaljokes = 0
prefix = 'http://onelinefun.com/'

for i in xrange(295):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    x = html.find_all('div', {'class': 'oneliner'})  
    jokes = [joke.find('p').get_text() for joke in x]
    for joke in jokes:
        joke = joke.replace('\n', '').replace('\t', '').replace('\r', '')
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))
f.close()
