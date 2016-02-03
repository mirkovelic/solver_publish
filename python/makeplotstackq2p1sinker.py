#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

#if len(sys.argv) > 1:
#    print sys.argv[1]

print "Usage:"
print "./makeplotstackq2p1sinker.py <res> <no_scale|scaled>\n"

res=sys.argv[1]
#jump=sys.argv[2]
scale=sys.argv[2]

pen3=[]
pen6=[]
pen9=[]
K3=[]
S3=[]
K6=[]
S6=[]
K9=[]
S9=[]

pre="../data/"
str3=pre+"plot_sinkerq2p1_%(res)s_%(jump)s_%(scale)s.txt" % {"res": res, "jump": "10e3", "scale": scale}
str6=pre+"plot_sinkerq2p1_%(res)s_%(jump)s_%(scale)s.txt" % {"res": res, "jump": "10e6", "scale": scale}
str9=pre+"plot_sinkerq2p1_%(res)s_%(jump)s_%(scale)s.txt" % {"res": res, "jump": "10e9", "scale": scale}


f = open(str3, "r")
for line in f:
    #print line
    #print line.split()[2]
    pen3.append(line.split()[0])
    #x2.append(line.split()[0])
    K3.append(line.split()[2])
    S3.append(line.split()[3])
f = open(str6, "r")
for line in f:
    #print line
    #print line.split()[2]
    pen6.append(line.split()[0])
    #x2.append(line.split()[0])
    K6.append(line.split()[2])
    S6.append(line.split()[3])
f = open(str9, "r")
for line in f:
    #print line
    #print line.split()[2]
    pen9.append(line.split()[0])
    #x2.append(line.split()[0])
    K9.append(line.split()[2])
    S9.append(line.split()[3])

minpen=1e-6
graphzero=str(minpen*0.1)
if float(pen3[0]) < minpen:
    pen3[0] = graphzero   # Want to include 0 penalty on the graph
if float(pen6[0]) < minpen:
    pen6[0] = graphzero   # Want to include 0 penalty on the graph
if float(pen9[0]) < minpen:
    pen9[0] = graphzero   # Want to include 0 penalty on the graph

print pen3[0]

lines = plt.loglog(pen3, S3, 'bs', pen3, K3, 'mo',pen6, S6, 'gs', pen6, K6, 'yo',pen9, S9, 'ks', pen9, K9, 'ro')
#lines = plt.plot(x, y, 'bs', x2, y2, 'ro')
#plt.xscale('log')
#plt.yscale('log')

str="Sinker Condition Numbers: $ %(res)s^2  \, $ %(scale)s\n Q2-P1 elements" % {"res": res, "scale": scale}
plt.title(str)

plt.xlabel("Penalty Number")
plt.ylabel("Condition Number")


dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
dashes = [5,2,10,5] # 5 points on, 2 off, 3 on, 1 off
for i in range(0,6,2):
    lines[i].set_dashes(dashes)
    lines[i+1].set_dashes(dashes)
plt.legend([lines[1], lines[0], lines[3], lines[2], lines[5], lines[4]], ["K $10^3$", "S $10^3$","K $10^6$", "S $10^6$", "K $10^9$", "S $10^9$"], loc='best', shadow=True )
plt.grid(True)
ticks=np.logspace(-7, 7, num=15)
print ticks

plt.xticks(ticks,('$0$','$10^{-6}$','$10^{-5}$','$10^{-4}$','$10^{-3}$','$10^{-2}$','$10^{-1}$','$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$','$10^{4}$','$10^{5}$','$10^{6}$','$10^{7}$'))

#plt.show()
d="../figs/sinker/"
if not os.path.exists(d):
    os.makedirs(d)

str=d+"stacksinkerq2p1ConditionNumbers%(res)s%(scale)s" % {"res": res, "scale": scale}
plt.savefig(str)
print str
#print x
#print y

#print x2
#print y2
