#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

if len(sys.argv) > 1:
    print sys.argv[1]

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

str3="plot_cxq2p1_%(res)s_%(jump)s_%(scale)s.txt" % {"res": res, "jump": "10e3", "scale": scale}
str6="plot_cxq2p1_%(res)s_%(jump)s_%(scale)s.txt" % {"res": res, "jump": "10e6", "scale": scale}
str9="plot_cxq2p1_%(res)s_%(jump)s_%(scale)s.txt" % {"res": res, "jump": "10e9", "scale": scale}

print str3

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


if float(pen3[0]) < 0.00001:
    pen3[0] = "0.001"   # Want to include 0 penalty on the graph
if float(pen6[0]) < 0.00001:
    pen6[0] = "0.001"   # Want to include 0 penalty on the graph
if float(pen9[0]) < 0.00001:
    pen9[0] = "0.001"   # Want to include 0 penalty on the graph

print pen3[0]

lines = plt.loglog(pen3, S3, 'bs', pen3, K3, 'ro',pen6, S6, 'gs', pen6, K6, 'mo',pen9, S9, 'ks', pen9, K9, 'yo')
#lines = plt.plot(x, y, 'bs', x2, y2, 'ro')
#plt.xscale('log')
#plt.yscale('log')

str="SolCx Condition Numbers: $ %(res)s^2  \, $ %(scale)s\n Q2-P1 elements" % {"res": res, "scale": scale}
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
ticks=np.logspace(-3, 7, num=11)
print ticks

plt.xticks(ticks,('$0$','$10^{-2}$','$10^{-1}$','$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$','$10^{4}$','$10^{5}$','$10^{6}$','$10^{7}$'))

#plt.show()
str="stacksolcxq2p1ConditionNumbers%(res)s%(scale)s" % {"res": res, "scale": scale}
plt.savefig(str)

#print x
#print y

#print x2
#print y2
