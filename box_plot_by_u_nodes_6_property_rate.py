#this code is specifically used for plotting
#a box plot for the all the zickle files 
#with 5 nodes
#which was created using liteqclass

#property: rate




import zickle as zkl
from matplotlib import pyplot as plt
import traversal, bfutils, graphkit, unknownrate,comparison
import numpy as np
from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes
import matplotlib.lines as mlines
from operator import add
import seaborn as sb

l = [
'mars_nodes_6_density_0.2_ral_.zkl',
'mars_nodes_6_density_0.25_ral_.zkl',
'oranos_nodes_6_density_0.3_ral_.zkl'
]

densities = [.2,.25,.3]
shift = 0
wds = 0.3
fliersz = 2
lwd = 1

#####################################################################################
def get_counts(d,U):
  rates = []
  for i in range(0,100):
    if len(d[i]['solutions'])>=U:
      if d[i]['solutions'][U]['eq']  == set([-1]): #supercliques
        rates.append(1000)  
      else:                                        #not a superclique
        s = d[i]['solutions'][U]['eq']
        H = bfutils.undersample(d[i]['gt'],U)
        all_rates = unknownrate.withrates(s,H).values()
        #print all_rates
        for rate in all_rates:
          rates.append(rate[0])
    else:#<U
      tempu = len(d[i]['solutions'])
      if d[i]['solutions'][tempu]['eq']  == set([-1]): #supercliques
        rates.append(1000)
      else:                                            #not a superclique
          s = d[i]['solutions'][tempu]['eq']
          H = bfutils.undersample(d[i]['gt'],tempu)
          all_rates = unknownrate.withrates(s,H).values()
          #print all_rates
          for rate in all_rates:
            rates.append(rate[0])   
  keys = np.sort(np.unique(rates))
  c = {}
  for k in keys:
    c[k] = len(np.where(rates == k)[0]) #key is rate and value is frequency
  #print c
  return c

def makeA(U):
  ulistofallrates = {}
  i = 0
  usz = set() #set of all rates that we have seen
  for fileitem in l: #each file is a dif density
    d = zkl.load(fileitem)
    c = get_counts(d,U)
    ulistofallrates[densities[i]] = c
    i = i + 1
    for v in c:
      usz.add(v)
  print usz
  for density in ulistofallrates:
    for rate in usz:
      if not rate in ulistofallrates[density]:
        ulistofallrates[density][rate] = 0


  A = []
  for density in densities:
    A.append([ulistofallrates[density][x] for x in np.sort(ulistofallrates[density].keys())])
  return A

####################################################
#u=2
#pre_A_2 = makeA(1)
#print "u2"
#print pre_A_2
pre_A_2 = [[1, 103, 3], [0, 103, 0], [0, 103, 0]]
mid_A_2 = [0]*len(pre_A_2[0])
for item in pre_A_2:
  mid_A_2 = np.add(item,mid_A_2)
post_A_2 = []
total = sum(mid_A_2)
for j in mid_A_2:
  post_A_2.append(j/float(total))

#u = 3 
#pre_A_3 = makeA(2)
#print "u3"
#print pre_A_3
pre_A_3 = [[1, 0, 129, 0, 0, 0, 0], [0, 0, 970, 0, 80, 16, 4], [0, 897, 267, 16, 15, 0, 0]]
mid_A_3 = [0]*len(pre_A_3[0])
for item in pre_A_3:
  mid_A_3 = np.add(item,mid_A_3)
post_A_3 = []
total = sum(mid_A_3)
for j in mid_A_3:
  post_A_3.append(j/float(total))

#u = 4
#pre_A_4 = makeA(3)
#print "u4"
#print pre_A_4
pre_A_4 = [[1, 26, 0, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 3429, 1493, 1095, 10, 260, 0, 108, 0, 77, 0, 0, 0, 0], [0, 9309, 15814, 5712, 1011, 254, 150, 25, 7, 1, 2, 1, 5, 1]]
mid_A_4 = [0]*len(pre_A_4[0])
for item in pre_A_4:
  mid_A_4 = np.add(item,mid_A_4)
post_A_4 = []
total = sum(mid_A_4)
for j in mid_A_4:
  post_A_4.append((j/float(total))*100)


#what do we want:
A = [post_A_2,post_A_3,post_A_4]

g1 = sb.boxplot(A,names=['2','3','4'],
               widths=wds,fliersize=fliersz,
               linewidth=lwd)

plt.xlabel('undersampling rate (u)')
plt.ylabel('percentage of graphs')
plt.title('n = 6,solution rates' ,multialignment='center')
g1.figure.get_axes()[0].set_yscale('log')


plt.savefig('bp_nodes_6_property_rate.svgz')
plt.show()

