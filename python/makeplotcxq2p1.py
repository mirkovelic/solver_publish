#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    print sys.argv[1]

if len(sys.argv) < 6:
    print "Usage: makeplot.py <res> <jump> <scale> <model> <elements>"
    print "e.g. makeplot.py 48 10e9 scaled cx q1p0"

res=sys.argv[1]
jump=sys.argv[2]
scale=sys.argv[3]
model=sys.argv[4]
elements=sys.argv[5]



x=[]
y=[]
x2=[]
y2=[]

str="../data/plot_%(model)s%(elements)s_%(res)s_%(jump)s_%(scale)s.txt" % {"model": model, "elements": elements, "res": res, "jump": jump, "scale": scale}

print str

f = open(str, "r")

#f.read()

for line in f:
    #print line
    #print line.split()[2]
    x.append(line.split()[0])
    x2.append(line.split()[0])
    y2.append(line.split()[2])
    y.append(line.split()[3])

#line, = plt.loglog(x, y, 'bo', linewidth=2, x, y2, 'r+', linewidth=2)
if float(x[0]) < 0.00001:
    x[0] = "0.001"
if float(x2[0]) < 0.00001:
    x2[0] = "0.001"

print x[0]
print x2[0]

lines = plt.loglog(x, y, 'bs', x2, y2, 'ro')
#lines = plt.plot(x, y, 'bs', x2, y2, 'ro')
#plt.xscale('symlog', linthresh=1.0e-60)
#plt.yscale('log')

str="Sol%(model)s Condition Numbers: $ %(res)s^2 \, \Delta\eta =  %(jump)s  \, $ %(scale)s\n %(elements)s elements" % {"model": model,  "elements": elements, "res": res, "jump": jump, "scale": scale}
plt.title(str)

plt.xlabel("Penalty Number")
plt.ylabel("Condition Number")


dashes = [10, 5, 100, 5] # 10 points on, 5 off, 100 on, 5 off
lines[0].set_dashes(dashes)
dashes = [5,2,10,5] # 5 points on, 2 off, 3 on, 1 off
lines[1].set_dashes(dashes)

plt.legend([lines[1], lines[0]], ["K", "S"],loc='best', shadow=True)

ticks=np.logspace(-3, 8, num=12)
print ticks

plt.xticks(ticks,('$0$','$10^{-2}$','$10^{-1}$','$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$','$10^{4}$','$10^{5}$','$10^{6}$','$10^{7}$','$10^{8}$'))

ticks=np.logspace(0, 10, num=11)
print ticks

plt.yticks(ticks,('$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$','$10^{4}$','$10^{5}$','$10^{6}$','$10^{7}$','$10^{8}$','$10^{9}$','$10^{10}$'))

#
#plt.show()
str="../figs/sol%(model)s/sol%(model)s%(elements)sConditionNumbers%(res)sJump%(jump)s%(scale)s" % {"model": model,  "elements": elements, "res": res, "jump": jump, "scale": scale}
plt.savefig(str)

#print x
#print y

#print x2
#print y2
