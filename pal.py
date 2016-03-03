# -*- coding: utf-8 -*-

import urllib
import string
import requests

#  Game: you arrive on a website and are given an a string of numbers
# 10 seconds to input numbers in ascending order to pass the level
#  run this in command line instead of using telnet to make it in 10s
# First time using urllib! yay :)

# URL taken from CTF in November 2015 - doesn't work anymore
f = urllib.urlopen("http://10.3.0.4/2bc37f8c51534ebe5787a46a17108522/")
# take all output and store as a string
raw = f.read()

# strips the string of everything that isn't numbers, standard string stuff
front = string.lstrip(raw,"Sort these: ")
back = string.rstrip(front,'.\n<form method="post">\
    <input type=“text" name="ascendingCommaSeparated"></input>\
    <input type="submit" /></form>')

# create a temporary var to store the numbers and sort them
almost = string.split(back,", ")
almost.sort(key=int)

# join the sorted numbers into a string, standard string stuff
new = string.join(almost,",")
print new

# send sorted string back to URL within 10s
data = {'ascendingCommaSeparated':new}
r = requests.post("http://10.3.0.4/2bc37f8c51534ebe5787a46a17108522/",
    data=data)
print data
print r.text
