'''
http://www.pythonchallenge.com/pc/def/oxygen.html
'''
import Image

fullimg = Image.open("../data/oxygen.png")
print fullimg.size
#img = fullimg.crop((0,0,629,95))
#print "info:",img.info
#print "mode:",img.mode
#print "bands:",img.getbands()


for i in range(43,52):
    txt = ""
    idx = 0
    img = fullimg.crop((0,i,629,i+1))
    for (a,b,c,d) in list(img.getdata()):
        if idx%7==0:
            txt += chr(a)
        idx += 1
    print txt
    print "".join([chr(x) for x in eval(txt[txt.find('['):txt.find(']')+1])])

#rband,gband,bband="","",""
#for (a,b,c,d) in list(img.getdata()):
#    rband += chr(a)
#    gband += chr(b)
#    bband += chr(c)
#print rband
#print gband
#print bband
