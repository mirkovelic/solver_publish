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

sv=[]
peny=[]

if scale == 'scaled':
    penalties = ["0", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1", "1", "10", "100", "1000", "10000", "100000", "1000000", "10000000"]
    toltest=0.00000001
    smallest=0.0000001
else:
    penalties = ["0", "0.01", "0.05", "0.1", "0.5", "1", "10", "100", "500", "1000", "10000", "100000", "1000000", "10000000"]
    toltest=0.01
    smallest=0.001

jump="10e9"
for pen in penalties:
    strx="spectrum_kxq2p1_%(res)s_%(jump)s_%(scale)s_%(pen)s.txt"% {"res": res, "jump": jump, "scale": scale, "pen": pen}
    print strx
    f = open(strx, "r")
    for line in f:
         sv.append(float(line.split()[0]))
         if float(pen) < toltest:
             pen = smallest
         peny.append(float(pen)*1.5)
         #print pen
    sv.pop()
    peny.pop()
    #sv=[]
    #peny=[]
plt.loglog(sv,peny,'b.', label="$\eta$ contrast=%s"%(jump))
    #plt.plot(sv,peny,'b.')

sv=[]
peny=[]
jump="10e6"
for pen in penalties:
    strx="spectrum_kxq2p1_%(res)s_%(jump)s_%(scale)s_%(pen)s.txt"% {"res": res, "jump": jump, "scale": scale, "pen": pen}
    print strx
    f = open(strx, "r")
    for line in f:
         sv.append(line.split()[0])
         if float(pen) < toltest:
             pen = smallest
         peny.append(float(pen))
         #print pen
    sv.pop()
    peny.pop()
#    plt.loglog(sv,peny,'c.')
#    sv=[]
#    peny=[]
plt.loglog(sv,peny,'c.',label="$\eta$ contrast=%s"%(jump))
    #plt.plot(sv,peny,'b.')
sv=[]
peny=[]
jump="10e3"
for pen in penalties:
    strx="spectrum_kxq2p1_%(res)s_%(jump)s_%(scale)s_%(pen)s.txt"% {"res": res, "jump": jump, "scale": scale, "pen": pen}
    print strx
    f = open(strx, "r")
    for line in f:
         sv.append(float(line.split()[0]))
         if float(pen) < toltest:
             pen = smallest
         peny.append(float(pen)*0.7)
         #print pen
    sv.pop()
    peny.pop()
    #plt.plot(sv,peny,'b.')
    #sv=[]
    #peny=[]
plt.loglog(sv,peny,'r.', label="$\eta$ contrast=%s"%(jump))

#exit();
#plt.yscale('log')
plt.legend(loc='best', ncol=1, shadow=True)
name="SolKx Schur Spectrum: $ %(res)s^2 $ %(scale)s\n Q2-P1 elements" % {"res": res, "scale": scale}
plt.title(name)

plt.xlabel("Eigenvalues")
plt.ylabel("Penalty Number")


#plt.legend([lines[1], lines[0], lines[3], lines[2], lines[5], lines[4]], ["K $10^3$", "S $10^3$","K $10^6$", "S $10^6$", "K $10^9$", "S $10^9$"], loc='best', shadow=True )
plt.grid(True)
#ticks=np.logspace(-3, 7, num=11)
#print ticks

#plt.xticks(ticks,('$0$','$10^{-2}$','$10^{-1}$','$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$','$10^{4}$','$10^{5}$','$10^{6}$','$10^{7}$'))

#plt.show()
name="spectrumstacksolkxq2p1ConditionNumbers%(res)s%(scale)sALL" % {"res": res, "scale": scale, "jump": str(jump)}
plt.savefig(name)

#print x
#print y

#print x2
#print y2
