#this code is specifically used for plotting
#a box plot for the zickle file 'saturn_nodes_5_density_0.25_ral_UMAX_11_.zkl'
#which was created using liteqclass



import seaborn as sb
import zickle as zkl
from matplotlib import pyplot as plt
import traversal, bfutils, graphkit, unknownrate,comparison

UMAX = 10
l = 'mars_nodes_5_density_0.25_UMAX_11_ral_.zkl'
shift = 0.15
wds = 0.3
fliersz = 2
lwd = 1

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
  time  = map(lambda x: x/1000./60., t)
  return time


d = zkl.load(l)
alltimes = []
mynames = []
for u in range(UMAX):
    partial_times = gettimes(d,u+1)  
    alltimes.append(partial_times)
    mynames.append(str(u+2))

g1 = sb.boxplot(alltimes,names=mynames,
               widths=wds,fliersize=fliersz,
               linewidth=lwd)

plt.xlabel('undersampling rate (u)')
plt.ylabel('computation time (minutes)')
plt.title('n = 5, number of graphs per u = 100, density = 25%' ,multialignment='center')
g1.figure.get_axes()[0].set_yscale('log')


plt.savefig('bp_nodes_5_density_.25_UMAX_11.svgz')
plt.show()
