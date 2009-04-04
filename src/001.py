'''
Created on Apr 4, 2009

@author: mturner
'''
from string import maketrans

q = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """

#def translate(c):
#    x = ord(c)
##    if x > 124: x -= 26
#    x += 2
#    return chr(x) 

intab = "".join([chr(x) for x in range(ord("a"),ord("z")+1)])
print intab
outtabarr = [chr(x) for x in range(ord("c"),ord("z")+1)]
outtabarr.append('a')
outtabarr.append('b')
outtab = "".join(outtabarr)
print outtab
trantab = maketrans(intab, outtab)
print q.translate(trantab)

print "map".translate(trantab)