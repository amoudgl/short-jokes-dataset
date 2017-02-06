# 
# 
# Scrapes all jokes from sql file downloaded from 
# Copyright (C) 2017  Abhinav Moudgil

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import csv
import sys

def parse_joke(line):
    # chop off sql command
    line = line[31:].rstrip().strip()[1:-2]
    x = line.split(",")
    # ignore first two elements, merge rest
    ans = ''
    for i in xrange(2, len(x)):
        ans = ans + x[i]
    # remove redundant chars
    ans = ans.replace('\\n', ' ').replace('\\r', '').replace("  ", " ").rstrip().strip()
    # remove quotes
    ans = ans.replace("\'\'", "'").replace("\'","'") 
    ans = ans[1:-1]
    return ans

f = open("../../data/funny_jokes.sql")
lines = f.readlines()
f.close()
filepath = '../../data/funjokes.csv'
f = open(filepath, 'a')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )
totaljokes = 0 
for i in xrange(len(lines)):
     totaljokes += 1
     writer.writerow((totaljokes, parse_joke(lines[i])))
f.close()

