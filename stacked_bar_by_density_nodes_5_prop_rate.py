#this code is specifically used for plotting
#a stacked bar graph for the all the zickle files 
#of a fixed number nodes = 5 and varying densities
#which was created using liteqclass

#instead of counting eqc sizes, counts different rates


import pylab as pl
import matplotlib as mpl
import seaborn as sns
import numpy as np
import zickle as zkl
from stackedBarGraph import StackedBarGrapher
import traversal, bfutils, graphkit, unknownrate,comparison
import zickle as zkl
from matplotlib import pyplot as plt
from matplotlib import gridspec
import random

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
def get_counts_2(d):
  rates = []
  for i in range(0,100):
    for U in range(1,len(d[i]['solutions'])+1):
      if d[i]['solutions'][U]['eq']  == set([-1]): #supercliques
        rates.append(1000)  
      else:                                        #not a superclique
        s = d[i]['solutions'][U]['eq']
        H = bfutils.undersample(d[i]['gt'],U)
        all_rates = unknownrate.withrates(s,H).values()
        #print all_rates
        for rate in all_rates:
          rates.append(rate[0])   
  keys = np.sort(np.unique(rates))
  c = {}
  for k in keys:
    c[k] = len(np.where(rates == k)[0]) #key is rate and value is frequency
  print c
  return c

def makeA_2():
  ulistofallrates = {}
  i = 0
  usz = set() #set of all rates that we have seen
  for fileitem in l: #each file is a dif density
    d = zkl.load(fileitem)
    c = get_counts_2(d)
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


# #############################################################################



#details for graphing

d_widths = [.5]*len(densities)
d_labels = []
for density in densities:
    d_labels.append(str(density))



#################################################################################
#pre_A = makeA_2()
pre_A = [
[12, 108, 108, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 2173, 2082, 402, 40, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 11873, 20021, 8779, 3187, 1314, 588, 406, 160, 147, 37, 108, 36, 4, 37, 48, 0], 
[0, 18322, 29127, 15775, 7444, 3378, 1839, 1784, 614, 421, 97, 318, 111, 7, 100, 312, 65], 
[0, 11164, 31736, 18807, 8003, 4886, 2738, 1443, 853, 848, 209, 165, 222, 4, 205, 168, 85], 
[0, 8380, 24305, 15795, 7229, 4146, 2390, 1972, 711, 635, 161, 300, 168, 4, 153, 312, 92]]
post_A = []
for i in pre_A:
  total = sum(i)
  post_A_partial = []
  for j in i:
    post_A_partial.append((j/float(total))*100)
  post_A.append(post_A_partial)

my_color_list = [
(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), 
(0.7645505989354233, 0.4875228836084111, 0.30496111115768654), 
(0.6151274326753975, 0.496189476149738, 0.75244053646953548), 
(0.1562085876188265, 0.44786703170340336, 0.9887241674046707), 
(0.4210506028639077, 0.2200011667972023, 0.37841949185273394), 
(0.7728656344058752, 0.17367399916287833, 0.026245548153039366), 
(0.904005064928743, 0.3038725882767085, 0.9399279068775889), 
(0.39140782566655674, 0.761012099948101, 0.7475874114794775), 
(0.0965359591761811, 0.43566457484639054, 0.9375581594394308), 
(0.859944654091911, 0.208070821188862, 0.8893517695418856), 
(0.022700048163251885, 0.658455757390323, 0.45194508876647577), 
(0.5934259725250017, 0.6259544064286037, 0.8943937276483482), 
(0.1248759682295419, 0.1286185769691658, 0.6973677590395778), 
(0.1834548561930609, 0.8625908063396674, 0.2808367027257399), 
(0.7072265637451247, 0.795648339142106, 0.4662593453344923), 
(0.9522043509564118, 0.8383482335114356, 0.04624824811210648), 
(0.2509444122476855, 0.723665792376911, 0.1685356796751546)] 


ax1 = plt.subplot2grid((7,7), (0,0), rowspan = 6, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax1,
                   post_A,
                   my_color_list,
                   xLabels=d_labels,
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(post_A)):
    Ai = [x for x in post_A[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 4.99:    
          pl.text(.5*i-0.02,yy-1.2,  str("%.2f" % Ai[j]),fontsize=12,zorder=10)


ax1.set_xticklabels(d_labels,rotation=0)
ax1.set_xlabel('densities')
ax1.set_title('n = 5, solution rates',multialignment='center')
ax1.set_ylabel('percentage of graphs',rotation = 90)












# ###################################LEGEND################################################
#helpful note:
#a(0)
#a+1
#a+2
#b(0) #b+1 #b+2
#the whole thing is divided into c by d blocks
#plt.subplot2grid((c,d), (a, b),rowspan = e, colspan = f)

ax2 = plt.subplot2grid((7,7), (6,2),rowspan =1,colspan=3)
bararray = [1,2,3,4,5,6]
rate_labels = ['1','2','3','4','5','6']
my_legend_color_list = [
my_color_list[0],
my_color_list[1],
my_color_list[2],
my_color_list[3],
my_color_list[4],
my_color_list[5]]
ax2.bar(bararray,[1]*6,color=my_legend_color_list,align='center')
ax2.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax2.axes.get_yaxis().set_visible(False)
ax2.set_xticklabels(rate_labels)
#ax2.set_axis_bgcolor('w')



######################################################################
ax3 = plt.subplot2grid((7,7), (6,5),rowspan =1,colspan=1)
bararray = [5,6]
rate_labels = ['16','S.C.']
my_legend_color_list = [
my_color_list[-2],
my_color_list[-1]]
ax3.bar(bararray,[1]*2,color=my_legend_color_list,align='center')
ax3.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax3.axes.get_yaxis().set_visible(False)
ax3.set_xticklabels(rate_labels)
#ax3.set_axis_bgcolor('w')





plt.text(4.1,0,"...")
plt.text(-4,0,"Rate")
plt.tight_layout()
plt.savefig('sb_nodes_5_property_rate.svgz')
plt.show()


