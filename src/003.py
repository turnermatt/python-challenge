'''
http://www.pythonchallenge.com/pc/def/equality.html
'''
import re

text = file("003.txt").read()

print "".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]",text))