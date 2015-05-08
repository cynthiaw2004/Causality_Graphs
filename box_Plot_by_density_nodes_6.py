#this code is specifically used for plotting
#a box plot for the all the zickle files 
#of a fixed number nodes and varying densities
#which was created using liteqclass




import zickle as zkl
from matplotlib import pyplot as plt
import traversal, bfutils, graphkit, unknownrate,comparison
import numpy as np
from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes
import matplotlib.lines as mlines

UMAX = 3 #u = 2,3,4
l = [
'mars_nodes_6_density_0.2_ral_.zkl',
'mars_nodes_6_density_0.25_ral_.zkl',
'oranos_nodes_6_density_0.3_ral_.zkl'
]
densities = [.2,.25,.3]


#######################################


def gettimes(d,U):
  t = []
  for i in range(0,100):
    if len(d[i]['solutions'])>=U:
    	if d[i]['solutions'][U]['eq']  == set([-1]): #supercliques
      		t.append(d[i]['solutions'][U-1]['ms']) 
    	else:
      		t.append(d[i]['solutions'][U]['ms'])
    else: #len of d[i]['solutions') < U
    	if d[i]['solutions'][len(d[i]['solutions'])]['eq']  == set([-1]): #supercliques
      		t.append(d[i]['solutions'][len(d[i]['solutions'])-1]['ms'])
    	else:
      		t.append(d[i]['solutions'][len(d[i]['solutions'])]['ms'])
  #print len(t)
  time  = map(lambda x: x/1000./60., t)
  return time

listofalltimes = []
for fileitem in l:
	d = zkl.load(fileitem)
	alltimes = []
	for u in range(UMAX):
		partial_times = gettimes(d,u+1)
		alltimes.append(partial_times)
	listofalltimes.append(alltimes)



#REFERENCE
#listofalltimes[0] = times for density 25
#listofalltimes[1] = times for density 30
#listofalltimes[2] = times for density 35


#listofalltimes[0][0] = times for density 25 with u = 2
#listofalltimes[0][1] =  times for density 25 with u = 3
#listofalltimes[0][2] = times for density 25 with u = 4


fig = figure()
ax = axes()
hold(True)


def boxsettings(bp):
	color = [(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), (0.6151274326753975, 0.4961389476149738, 0.15244053646953548)]
	i = 0
	for box in bp['boxes']:
		box.set( color='#000000', linewidth=1)
	    	box.set(facecolor = color[i] )
		i = i +1


	for whisker in bp['whiskers']:
		whisker.set(color='#000000',linewidth=1,ls = '-')


	for cap in bp['caps']:
		cap.set(color='#000000', linewidth=1)


	for median in bp['medians']:
		median.set(color='#000000', linewidth=1)


	for flier in bp['fliers']:
		flier.set(color='#000000', alpha=0.5,marker = 'o',markersize = 1.5)


# first boxplot pair density 250%
bp = boxplot(listofalltimes[0], positions = [1, 2, 3],widths = 0.6,patch_artist = True)
boxsettings(bp)

# second boxplot pair density 25%
bp = boxplot(listofalltimes[1], positions = [6, 7, 8], widths = 0.6,patch_artist = True,)
boxsettings(bp)

# thrid boxplot pair density 30%
bp = boxplot(listofalltimes[2], positions = [11,12,13], widths = 0.6,patch_artist = True)
boxsettings(bp)






# set axes limits and labels
xlim(0,14)
ax.set_xticklabels(['20%', '25%', '30%'])
ax.set_xticks([2,7,12])
ax.set_yscale('log')
ax.yaxis.grid(color='w',ls = '-')
ax.set_axis_bgcolor((.93,.93,1))
ax.set_axisbelow(True)

#legend
color = [(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), (0.6151274326753975, 0.4961389476149738, 0.15244053646953548)]
u2 = mlines.Line2D([], [], color=color[0], marker='s',
                          markersize=15, markeredgewidth = 1,label='u = 2')
u3 = mlines.Line2D([], [], color=color[1], markeredgewidth = 1,marker='s',
                          markersize=15, label='u = 3')
u4 = mlines.Line2D([], [], color=color[2], markeredgewidth = 1,marker='s',
                          markersize=15, label='u = 4')
plt.legend(handles=[u2,u3,u4],numpoints = 1,loc = 0)


plt.xlabel('densities')
plt.ylabel('computation time (minutes)')
plt.title('n = 6, number of graphs per u = 100' ,multialignment='center')

plt.savefig('bp_nodes_6.svgz')
plt.show()
