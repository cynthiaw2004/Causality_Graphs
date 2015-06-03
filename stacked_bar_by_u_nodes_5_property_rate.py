#this code is specifically used for plotting
#a stacked bar plot for the all the zickle files 
#with 5 nodes
#which was created using liteqclass

#property: rate



import pylab as pl
import zickle as zkl
from matplotlib import pyplot as plt
import traversal, bfutils, graphkit, unknownrate,comparison
import numpy as np
from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes
import matplotlib.lines as mlines
from operator import add
from stackedBarGraph import StackedBarGrapher
import seaborn as sns


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
  print "!"
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
#to keep lengths same as other pre_A_u's
for item in pre_A_2:
  while len(item) != 17: #in the interest of time, done manually to get 17 but can be coded up better
    item.append(0)
mid_A_2 = [0]*len(pre_A_2[0])
for item in pre_A_2:
  mid_A_2 = np.add(item,mid_A_2)
post_A_2 = []
total = sum(mid_A_2)
for j in mid_A_2:
  post_A_2.append(j/float(total)*100)

print "u = 2"
print post_A_2
print sum(post_A_2)

#u = 3 
#pre_A_3 = makeA(2)
#print "u3"
#print pre_A_3
pre_A_3 = [[4, 4, 100, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 5, 104, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 96, 147, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 14618, 17500, 6849, 3242, 1145, 567, 654, 219, 97, 24, 126, 27, 5, 24, 120, 3], [0, 10191, 26556, 14701, 6381, 3520, 1953, 1135, 629, 570, 149, 141, 150, 4, 143, 144, 16], [0, 6056, 21533, 13362, 5997, 3440, 1951, 1455, 598, 544, 141, 210, 144, 4, 130, 216, 39]]
mid_A_3 = [0]*len(pre_A_3[0])
for item in pre_A_3:
  mid_A_3 = np.add(item,mid_A_3)
post_A_3 = []
total = sum(mid_A_3)
for j in mid_A_3:
  post_A_3.append(j/float(total)*100)

print "u = 3"
print post_A_3
print sum(post_A_3)

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

print "u = 4"
print post_A_4
print sum(post_A_4)

#what do we want:
A = [post_A_2,post_A_3,post_A_4]

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

d_widths = [.5]*len(['2','3','4'])


ax1 = plt.subplot2grid((7,7), (0,0), rowspan = 6, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax1,
                   A,
                   my_color_list,
                   xLabels=['2','3','4'],
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(A)):
    Ai = [x for x in A[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 4.99:    
          pl.text(.5*i-0.02,yy-1.2,  str("%.2f" % Ai[j]),fontsize=12,zorder=10)


ax1.set_xticklabels(['2','3','4'],rotation=0)
ax1.set_xlabel('undersampling rate (u)')
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
plt.savefig('sb_nodes_5_by_u_property_rate.svgz')
plt.show()




