#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import re

print "Usage:"

pits=[]
cons=[]
pen=[]
pc=[]
scaled=[]
res=[]
jump=[]

filestr=sys.argv[1]
stride=int(sys.argv[2])
offset=int(sys.argv[3])

pre="../data/"

p = re.compile(r"""^\|\s*(?P<pits>\d+)\s*\|           #get Pressure iterations
                      \s*(\d+)\s*\|
                      \s*(?P<ptime>\d+\.\d+)\s*\|     # total pressure solve time (secs)
                     (?P<cons>\s*[\w\.\-]+\s*)\|      # constraint value
                    ((?P<pen>\s*[ \.\-\w]+\s*)\|){8}  # penalty number
                    (?P<pc>\s*[\.\-\w]+\s*)\|         # preconditioner
                    \s*(?P<scaled>\d+)\s*\|           # scaling
                    (\s*(?P<res>[\.\-\w]+)\s*\|){6}   # resolution
                    ((?P<jump>\s*[\.\-\w]+\s*)\|){4}  # viscosity constrast
     """, re.VERBOSE)
f = open(filestr, "r")
for line in f:
    #print line
    m = p.match(line)
    if m != None:
        print m.group('pits'), m.group('cons'),  m.group('pen'), m.group('pc'), m.group('scaled'), m.group('res'), m.group('jump')
        pits.append(m.group('pits'))
        cons.append(m.group('cons'))
        pen.append(m.group('pen'))
        scaled.append(m.group('scaled'))
        res.append(m.group('res'))

lines = plt.plot(pen[0+offset:stride+offset], pits[0+offset:stride+offset], 'bs')
plt.xscale('log')
plt.grid(True)
str="pen%(res)s%(scale)s" % {"res": res[offset], "scale": scaled[offset]}
plt.savefig(str)

plt.close()
lines = plt.loglog(pen[0+offset:stride+offset], cons[0+offset:stride+offset], 'bs')
plt.grid(True)
str="consRes=%(res)sScaled=%(scale)s" % {"res": res[offset], "scale": scaled[offset]}
plt.savefig(str)

#print len(pits)

#    print m.group(2)
#    print m.group(3)
