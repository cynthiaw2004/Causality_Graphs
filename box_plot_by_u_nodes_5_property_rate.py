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
'oranos_nodes_5_density_0.25_ral_.zkl',
'oranos_nodes_5_density_0.3_ral_.zkl',
'oranos_nodes_5_density_0.35_ral_.zkl',
'oranos_nodes_5_density_0.4_ral_.zkl',
'jupiter_nodes_5_density_0.45_ral_.zkl',
'neptune_nodes_5_density_0.5_ral_.zkl',
]

densities = [.25,.3,.35,.4,.45,.5]
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
pre_A_2 = [[4, 100, 4, 4, 0], [0, 100, 0, 0, 0], [0, 104, 0, 0, 0], [0, 206, 4, 0, 0], [0, 436, 16, 0, 1], [0, 2267, 543, 70, 0]]
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
#FIX INCORRECT
pre_A_3 = [[4, 4, 100, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 5, 104, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 96, 147, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 14618, 17500, 6849, 3242, 1145, 567, 654, 219, 97, 24, 126, 27, 5, 24, 120, 3], [0, 10191, 26556, 14701, 6381, 3520, 1953, 1135, 629, 570, 149, 141, 150, 4, 143, 144, 16], [0, 6056, 21533, 13362, 5997, 3440, 1951, 1455, 598, 544, 141, 210, 144, 4, 130, 216, 39]]
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
pre_A_4 = [[4, 4, 4, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2068, 1978, 402, 40, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 11673, 19874, 8777, 3187, 1314, 588, 406, 160, 147, 37, 108, 36, 4, 37, 48, 0], [0, 3498, 11623, 8926, 4202, 2233, 1272, 1130, 395, 324, 73, 192, 84, 2, 76, 192, 65], [0, 537, 5164, 4106, 1621, 1366, 785, 308, 224, 278, 60, 24, 72, 0, 62, 24, 85], [0, 57, 2229, 2363, 1232, 706, 439, 517, 113, 91, 20, 90, 24, 0, 23, 96, 92]]
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
plt.title('n = 5,solution rates' ,multialignment='center')
g1.figure.get_axes()[0].set_yscale('log')


plt.savefig('bp_nodes_5_property_rate.svgz')
plt.show()

