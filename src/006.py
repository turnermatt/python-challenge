'''
http://www.pythonchallenge.com/pc/def/channel.html

hint1: start from 90052
hint2: answer is inside the zip
'''
import urllib
import zipfile

zip = zipfile.ZipFile("../data/channel.zip",'r')

nothing = "90052"
comments = []
while True:
    text = zip.read(nothing + ".txt")
    print text,":", zip.getinfo(nothing+".txt").comment
    if not text.startswith("Next nothing is") or not text.split()[3].isdigit():
        break
    else:
        comments.append(zip.getinfo(nothing+".txt").comment)
        nothing = text.split()[-1]
print "".join(comments)

