'''
http://www.pythonchallenge.com/pc/def/linkedlist.html
http://www.pythonchallenge.com/pc/def/linkedlist.php
'''
import urllib

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "33179"
nothings = []
text = ""
repeat_count = 0
for i in range(400):
    handle = urllib.urlopen(baseurl+nothing)
    text = handle.read()
    print i, ":", nothing, ":", text
    if nothing in nothings:
        print "repeat"
        repeat_count += 1
        if repeat_count >10: break
    else:
        nothings.append(nothing)
    if " ".join(text.split()[:-1]) != "and the next nothing is":
        print text
    if text == "Yes. Divide by two and keep going.":
        print nothing
        nothing = str(int(nothing)/2)
        print nothing
    else:
        nothing = text.split()[-1]
        if not nothing.isdigit(): break

print text