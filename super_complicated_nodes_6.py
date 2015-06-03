#6 nodes

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
'mars_nodes_6_density_0.2_ral_.zkl',
'mars_nodes_6_density_0.25_ral_.zkl',
'oranos_nodes_6_density_0.3_ral_.zkl'
]

#densities:.2,.25.,.3
#undersampling:2,3,4 (insert 1,2,3)
def get_subplot_x_y(density_of_gt_file,undersampling):
    d = zkl.load(density_of_gt_file)
    x = []
    y = []
    for i in range(0,100):
        g2 = bfutils.undersample(d[i]['gt'],undersampling)   #this is H
        x.append(traversal.density(g2))          #add the density of H
        y.append(d[i]['solutions'][undersampling]['ms'])     #add the time
    return x,y

#################################

#d = .2, u = 2 (inner labels included)
x,y = get_subplot_x_y(L[0],1)
ax1 = plt.subplot2grid((20,11), (0,0), rowspan = 20, colspan=1)
ax1 = plt.gca()
ax1.scatter(x,y)
ax1.set_yscale('log')
ax1.set_xlabel('2')
ax1.set_ylabel('Run Time')
ax1.set_xlim(0,1)
ax1.set_ylim(10**1,10**8)
empty_string_labels_x = ['']*5
ax1.set_xticklabels(empty_string_labels_x)



#d = .2, u = 3
x,y = get_subplot_x_y(L[0],2)
ax2 = plt.subplot2grid((20,11), (0,1), rowspan = 20, colspan=1)
ax2 = plt.gca()
ax2.scatter(x,y)
ax2.set_yscale('log')
ax2.set_xlim(0,1)
ax2.set_ylim(10**1,10**8)
ax2.set_xticklabels(empty_string_labels_x)
empty_string_labels_y = ['']*8
ax2.set_yticklabels(empty_string_labels_y)
ax2.set_xlabel('3')
ax2.set_title('20%',multialignment='center')




#d = .2, u = 4
x,y = get_subplot_x_y(L[0],3)
ax3 = plt.subplot2grid((20,11), (0,2), rowspan = 20, colspan=1)
ax3 = plt.gca()
ax3.scatter(x,y)
ax3.set_yscale('log')
ax3.set_xlim(0,1)
ax3.set_ylim(10**1,10**8)
ax3.set_xticklabels(empty_string_labels_x)
ax3.set_yticklabels(empty_string_labels_y)
ax3.set_xlabel('4')


####################################
#d = .25, u = 2
x,y = get_subplot_x_y(L[1],1)
ax4 = plt.subplot2grid((20,11), (0,4), rowspan = 20, colspan=1)
ax4 = plt.gca()
ax4.scatter(x,y)
ax4.set_yscale('log')
ax4.set_xlim(0,1)
ax4.set_ylim(10**1,10**8)
ax4.set_xticklabels(empty_string_labels_x)
ax4.set_yticklabels(empty_string_labels_y)
ax4.set_xlabel('2')


#d = .25, u = 3
x,y = get_subplot_x_y(L[1],2)
ax5 = plt.subplot2grid((20,11), (0,5), rowspan = 20, colspan=1)
ax5 = plt.gca()
ax5.scatter(x,y)
ax5.set_yscale('log')
ax5.set_xlim(0,1)
ax5.set_ylim(10**1,10**8)
ax5.set_xticklabels(empty_string_labels_x)
ax5.set_yticklabels(empty_string_labels_y)
ax5.set_xlabel('3 \n undersampling')
ax5.set_title('Density of G \n 25%',multialignment='center')



#d = .25, u = 4
x,y = get_subplot_x_y(L[1],3)
ax6 = plt.subplot2grid((20,11), (0,6), rowspan = 20, colspan=1)
ax6 = plt.gca()
ax6.scatter(x,y)
ax6.set_yscale('log')
ax6.set_xlim(0,1)
ax6.set_ylim(10**1,10**8)
ax6.set_xticklabels(empty_string_labels_x)
ax6.set_yticklabels(empty_string_labels_y)
ax6.set_xlabel('4')


############################
#d = .3, u = 2
x,y = get_subplot_x_y(L[2],1)
ax7 = plt.subplot2grid((20,11), (0,8), rowspan = 20, colspan=1)
ax7 = plt.gca()
ax7.scatter(x,y)
ax7.set_yscale('log')
ax7.set_ylim(10**1,10**8)
ax7.set_xlim(0,1)
ax7.set_xticklabels(empty_string_labels_x)
ax7.set_yticklabels(empty_string_labels_y)
ax7.set_xlabel('2')


#d = .3, u = 3
x,y = get_subplot_x_y(L[2],2)
ax8 = plt.subplot2grid((20,11), (0,9), rowspan = 20, colspan=1)
ax8 = plt.gca()
ax8.scatter(x,y)
ax8.set_yscale('log')
ax8.set_ylim(10**1,10**8)
ax8.set_xlim(0,1)
ax8.set_xticklabels(empty_string_labels_x)
ax8.set_yticklabels(empty_string_labels_y)
ax8.set_xlabel('3')
ax8.set_title('30%',multialignment='center')



#d = .3, u = 4
x,y = get_subplot_x_y(L[2],3)
ax9 = plt.subplot2grid((20,11), (0,10), rowspan = 20, colspan=1)
ax9 = plt.gca()
ax9.scatter(x,y)
ax9.set_yscale('log')
ax9.set_ylim(10**1,10**8)
ax9.set_xlim(0,1)
ax9.set_xticklabels(empty_string_labels_x)
ax9.set_yticklabels(empty_string_labels_y)
ax9.set_xlabel('4')




plt.text(-11.9,13," .2 .4 .6 .8",fontsize=6)


plt.savefig('super_complicated_nodes_6.svgz')
plt.show()

