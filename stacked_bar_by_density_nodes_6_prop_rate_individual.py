#this code is specifically used for plotting
#a stacked bar graph for the all the zickle files 
#of a fixed number nodes = 6 and varying densities
#which was created using liteqclass

#instead of counting eqc sizes, counts different rates
#individual graphs for u=2,3,4


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


# #############################################################################



#details for graphing

d_widths = [.5]*len(densities)
d_labels = []
for density in densities:
    d_labels.append(str(density))



#################################################################################
#graph subplot for u=2
#pre_A_2 = makeA(1)
#print "u2"
#print pre_A_2
pre_A_2 = [[1, 103, 3], [0, 103, 0], [0, 103, 0]]
post_A_2 = []
for i in pre_A_2:
  total = sum(i)
  post_A_partial = []
  for j in i:
    post_A_partial.append((j/float(total))*100)
  post_A_2.append(post_A_partial)

my_color_list_2 = [
(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), 
(0.7645505989354233, 0.4875228836084111, 0.30496111115768654),  
(0.1562085876188265, 0.44786703170340336, 0.9887241674046707), ]


ax1 = plt.subplot2grid((20,7), (0,0), rowspan = 4, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax1,
                   post_A_2,
                   my_color_list_2,
                   xLabels=d_labels,
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(post_A_2)):
    Ai = [x for x in post_A_2[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 4.99:    
          pl.text(.5*i-0.02,yy-1.2,  str("%.2f" % Ai[j]),fontsize=12,zorder=10)




ax1.set_title('n = 6, solution rates',multialignment='center')
ax1.set_ylabel('u = 2',rotation = 90)
ax1.axes.get_xaxis().set_visible(False)

#########################################################################################
#graph subplot for u=3
#pre_A_3 = makeA(2)
#print "u3"
#print pre_A_3
pre_A_3 = [[1, 0, 129, 0, 0, 0, 0], [0, 0, 970, 0, 80, 16, 4], [0, 897, 267, 16, 15, 0, 0]]
post_A_3 = []
for i in pre_A_3:
  total = sum(i)
  post_A_partial = []
  for j in i:
    post_A_partial.append((j/float(total))*100)
  post_A_3.append(post_A_partial)

my_color_list_3 = [
(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), 
(0.7645505989354233, 0.4875228836084111, 0.30496111115768654), 
(0.6151274326753975, 0.496189476149738, 0.75244053646953548), 
(0.1562085876188265, 0.44786703170340336, 0.9887241674046707), 
(0.4210506028639077, 0.2200011667972023, 0.37841949185273394), 
(0.904005064928743, 0.3038725882767085, 0.9399279068775889), 
(0.0965359591761811, 0.43566457484639054, 0.9375581594394308)] 


ax2 = plt.subplot2grid((20,7), (5,0), rowspan = 4, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax2,
                   post_A_3,
                   my_color_list_3,
                   xLabels=d_labels,
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(post_A_3)):
    Ai = [x for x in post_A_3[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 13:    
          pl.text(.5*i-0.02,yy-1.2,  str("%.2f" % Ai[j]),fontsize=12,zorder=10)


ax2.set_ylabel('percentage of graphs \n u = 3',rotation = 90)
ax2.axes.get_xaxis().set_visible(False)

#########################################################################
#graph subplot for u=4
#pre_A_4 = makeA(3)
#print "u4"
#print pre_A_4
pre_A_4 = [[1, 26, 0, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 3429, 1493, 1095, 10, 260, 0, 108, 0, 77, 0, 0, 0, 0], [0, 9309, 15814, 5712, 1011, 254, 150, 25, 7, 1, 2, 1, 5, 1]]
post_A_4 = []
for i in pre_A_4:
  total = sum(i)
  post_A_partial = []
  for j in i:
    post_A_partial.append((j/float(total))*100)
  post_A_4.append(post_A_partial)

my_color_list_4 = [
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
(0.5934259725250017, 0.6259544064286037, 0.8943937276483482), 
(0.1834548561930609, 0.8625908063396674, 0.2808367027257399), 
(0.9522043509564118, 0.8383482335114356, 0.04624824811210648), 
(0.2509444122476855, 0.723665792376911, 0.1685356796751546)] 


ax3 = plt.subplot2grid((20,7), (11,0), rowspan = 4, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax3,
                   post_A_4,
                   my_color_list_4,
                   xLabels=d_labels,
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(post_A_4)):
    Ai = [x for x in post_A_4[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 10:    
          pl.text(.5*i-0.02,yy-1.2,  str("%.2f" % Ai[j]),fontsize=12,zorder=10)

ax3.set_xlabel('densities',rotation = 0)
ax3.set_ylabel('u = 4',rotation = 90)
ax3.set_xticklabels(d_labels,rotation=0)







# ###################################LEGEND################################################
#helpful note:
#a(0)
#a+1
#a+2
#b(0) #b+1 #b+2
#the whole thing is divided into c by d blocks
#plt.subplot2grid((c,d), (a, b),rowspan = e, colspan = f)

full_color_list = [
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
(0.5934259725250017, 0.6259544064286037, 0.8943937276483482), 
(0.1834548561930609, 0.8625908063396674, 0.2808367027257399), 
(0.9522043509564118, 0.8383482335114356, 0.04624824811210648), 
(0.2509444122476855, 0.723665792376911, 0.1685356796751546)] 


ax4 = plt.subplot2grid((20,7), (19,1),colspan=3,rowspan = 1)
bararray = [1,2,3,4,5,6]
rate_labels = ['1','2','3','4','5','6']
my_legend_color_list = [
full_color_list[0],
full_color_list[1],
full_color_list[2],
full_color_list[3],
full_color_list[4],
full_color_list[5]]
ax4.bar(bararray,[1]*6,color=my_legend_color_list,align='center')
ax4.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax4.axes.get_yaxis().set_visible(False)
ax4.set_xticklabels(rate_labels)
ax4.set_axis_bgcolor('w')



######################################################################
ax5 = plt.subplot2grid((20,7), (19,4),colspan=1,rowspan=1)
bararray = [5,6]
rate_labels = ['16','S.C.']
my_legend_color_list = [
full_color_list[-2],
full_color_list[-1]]
ax5.bar(bararray,[1]*2,color=my_legend_color_list,align='center')
ax5.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax5.axes.get_yaxis().set_visible(False)
ax5.set_xticklabels(rate_labels)#ax5.set_axis_bgcolor('w')











plt.text(3.9,0,"...")
plt.text(-4,0,"Rate")
plt.savefig('sb_nodes_6_property_rate_individual.svgz')
plt.show()


