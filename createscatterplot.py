import sys,os
sys.path.append('./tools/')
from multiprocessing import Pool,Process, Queue, cpu_count, current_process
import functools
import zickle as zkl
import time, socket
import scipy
import zickle as zkl
import traversal, bfutils, graphkit, unknownrate
import bfutils as bfu

import matplotlib.pyplot as plt

NODES = 6
DENSITY = 0.2
UMAX = 6
REPEATS = 100


d = zkl.load('leibnitz_nodes_6_density_0.2_ra_.zkl')

x = []
y = []

for i in range(0,REPEATS):
    gs = bfutils.call_undersamples(d[i]['gt'])   #this helps us determine how far u will go
    for u in range(1,min([len(gs),UMAX])):
        g2 = bfutils.undersample(d[i]['gt'],u)   #this is H
        x.append(traversal.density(g2))          #add the density of H
        y.append(d[i]['solutions'][u]['ms'])     #add the time

print len(x)
print len(y)
fig = plt.figure()
ax = plt.gca()
ax.scatter(x,y)
ax.set_yscale('log')
plt.xlabel('edge density of H')
plt.ylabel('log scale time')
plt.title('Number of Nodes: %s , Density: %s ,UMAX: %s'%(NODES,DENSITY,UMAX))
plt.xlim(0,1)
plt.show()

