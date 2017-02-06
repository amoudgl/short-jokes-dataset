# merge_csvs.py
# Merges all csv files from /data/ folder into a single csv file, 
# removing duplicates on the fly
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

import json
import os
import csv

folder_path = '../data/'
files = os.listdir(folder_path)

# extract all jokes in a singe list
all_jokes = []
for filename in files:
    filepath = folder_path + filename
    f = open(filepath)
    reader = csv.reader(f)
    for row in reader:
        all_jokes.append(row[1])
    f.close()
print ("Initial dataset size = %d" % (len(all_jokes)))

# ignore jokes with more than 200 characters
all_jokes = [joke for joke in all_jokes if len(joke) >= 10 and len(joke) <= 200]
print ("Ignoring long jokes, dataset size = %d" % (len(all_jokes)))

# Remove duplicates
all_jokes = list(set(all_jokes))
print ("Removed duplicates, dataset size = %d" % (len(all_jokes)))

# write all jokes to csv file
idx = 0
filepath = '../shortjokes.csv'
f = open(filepath, 'w')
writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow( ('ID', 'Joke') )
for joke in all_jokes:
    if (len(joke) >= 10 and len(joke) <= 200):
        idx += 1
        writer.writerow((idx, joke))
f.close()
