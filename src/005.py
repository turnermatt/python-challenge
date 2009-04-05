'''
http://www.pythonchallenge.com/pc/def/peak.html
'''
import urllib
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
handle = urllib.urlopen(url)

p = pickle.load(handle)
for l in p:
    out = ""
    for (char, count) in l:
        for i in range(count):
            out += char
    print out
