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



L = [
'jupiter_nodes_7_density_0.2_ral_.zkl'
]

def gen_x_y(L):
    x = []
    y = []
    for l in L:
        d = zkl.load(l)
        for i in range(0,100):
            gs = bfutils.call_undersamples(d[i]['gt'])   #this helps us determine how far u will go
            for u in range(1,len(d[i]['solutions'])+1):
            #for u in range(1,min([len(gs),4])):
                g2 = bfutils.undersample(d[i]['gt'],u)   #this is H
                x.append(traversal.density(g2))          #add the density of H
                y.append(d[i]['solutions'][u]['ms'])     #add the time

    return x,y

x,y = gen_x_y(L)
fig = plt.figure()
ax = plt.gca()
ax.scatter(x,y)
ax.set_yscale('log')
plt.xlabel('density of H')
plt.ylabel('log scale computation time')
plt.title('n = 7')
plt.xlim(0,1)
plt.ylim(10*2,10**5)
plt.savefig('H_dens_vs_log_time_nodes_7.svgz')
plt.show()

