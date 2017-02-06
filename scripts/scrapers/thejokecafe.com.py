# thejokecafe.com.py
# Scrapes jokes from http://thejokecafe.com/ and and save them to csv file
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

filepath = '../../data/thejokecafe.csv'
f = open(filepath, 'w')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )
totaljokes = 0
prefix = 'http://thejokecafe.com/funny-one-liners/'

for i in xrange(57):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    content = html.find_all('ol')
    jokes = content[0].find_all('li')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...")
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

prefix = 'http://thejokecafe.com/short-jokes/'
for i in xrange(50):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    content = html.find_all('ol')
    jokes = content[0].find_all('li')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

prefix = 'http://thejokecafe.com/funny-whatsapp-status/'
for i in xrange(68):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    content = html.find_all('ol')
    jokes = content[0].find_all('li')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

prefix = 'http://thejokecafe.com/humorous-quotes/'
for i in xrange(56):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    content = html.find_all('ol')
    jokes = content[0].find_all('li')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

prefix = 'http://thejokecafe.com/funny-sayings/'
for i in xrange(50):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    content = html.find_all('ol')
    jokes = content[0].find_all('li')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

prefix = 'http://thejokecafe.com/funny-quotes-for-facebook/'
for i in xrange(8):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    content = html.find_all('ol')
    jokes = content[0].find_all('li')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

prefix = 'http://thejokecafe.com/funny-posts/'
for i in xrange(37):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    content = html.find_all('ol')
    jokes = content[0].find_all('li')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

prefix = 'http://thejokecafe.com/category/wordplay-puns-jokes/page/'
for i in xrange(242):
    url = prefix + str(i + 1) + '/'
    r = urllib.urlopen(url).read()
    html = bs(r, 'html.parser')
    jokes = html.find_all('p')
    jokes = [joke.get_text() for joke in jokes]
    for joke in jokes:
        joke = joke.replace('\n', " ").replace("\r", " ").replace("\t", " ").replace("    ", " ").replace("  ", " ").rstrip().strip().replace("  ", " ")
        joke = joke.replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2019", "'").replace(u"\u2026", "...") 
        joke = unicodedata.normalize('NFKD', joke).encode('ascii','ignore')
        totaljokes += 1
        writer.writerow((totaljokes, joke))
    print ("Page %d processed, total number of jokes = %d" %(i + 1, totaljokes))

f.close()
