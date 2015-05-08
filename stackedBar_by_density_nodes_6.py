#this code is specifically used for plotting
#a stacked bar graph for the all the zickle files 
#of a fixed number nodes = 5 and varying densities
#which was created using liteqclass


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


UMAX = 3 #u = 2,3,4
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
  eqc = []
  for i in range(0,100):
    if len(d[i]['solutions'])>=U:
    	if d[i]['solutions'][U]['eq']  == set([-1]): #supercliques
		eqc.append(1001)
    	else:
      		eqc.append(len(d[i]['solutions'][U]['eq']))
    else:
	tempu = len(d[i]['solutions'])
    	if d[i]['solutions'][tempu]['eq']  == set([-1]): #supercliques
		eqc.append(1001)
    	else:
      		eqc.append(len(d[i]['solutions'][tempu]['eq']))
  keys = np.sort(np.unique(eqc))
  c = {}
  for k in keys:
    c[k] = len(np.where(eqc == k)[0]) #key is equiv class size and value is frequency
  print "\n"
  return c

def makeA(u):
  ulistofalldensities = {}
  i = 0
  usz = set() #set of all equivalence class sizes that we have seen
  for fileitem in l: #each file is a dif density
    d = zkl.load(fileitem)
    c = get_counts(d,u)
    ulistofalldensities[densities[i]] = c
    i = i + 1
    for v in c:
      usz.add(v)
  print usz
  #print ulistofalldensities

  #print usz
  for density in ulistofalldensities:
    for size in usz:
      if not size in ulistofalldensities[density]:
        ulistofalldensities[density][size] = 0

  A = []
  for density in densities:
    A.append([ulistofalldensities[density][x] for x in np.sort(ulistofalldensities[density].keys())])
  return A



#############################################################################



#details for graphing all subplots

d_widths = [.5]*len(densities)
d_labels = []
for density in densities:
    d_labels.append(str(density))



#################################################################################
#graph subplot for u  = 2
A2 = makeA(1)
mycolorlistu2 = [(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), (0.39140782566655674, 0.7613012099948101, 0.7475874114794775)]



ax1 = plt.subplot2grid((20,7), (0,0), rowspan = 5, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax1,
                   A2,
                   mycolorlistu2,
                   xLabels=d_labels,
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(A2)):
    Ai = [x for x in A2[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 10:    
          pl.text(0.5*i-0.02,yy-1.2,str(Ai[j]),fontsize=12,zorder=10)

ax1.axes.get_xaxis().set_visible(False)
ax1.set_title('n = 6, number of graphs per u = 100',multialignment='center')
ax1.set_ylabel('u = 2',rotation = 90)





#graph subplot for u = 3
A3 = makeA(2)
mycolorlistu3 = [(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), (0.6151274326753975, 0.4961389476149738, 0.15244053646953548), (0.1562085876188265, 0.44786703170340336, 0.9887241674046707), (0.4210506028639077, 0.22000131667972023, 0.37841949185273394), (0.7728656344058752, 0.47367399916287833, 0.026245548153039366), (0.39140782566655674, 0.7613012099948101, 0.7475874114794775), (0.09653595917613811, 0.43566457484639054, 0.9375581594394308), (0.2509444122476855, 0.7236657923769131, 0.1685356796751546), (0.485805564023866, 0.47863413192322646, 0.6321014062281413), (0.9241714458529445, 0.8143896488420276, 0.7663922292951993)]



ax2 = plt.subplot2grid((20,7), (5,0), rowspan = 5, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax2,
                   A3,
                   mycolorlistu3,
                   xLabels=d_labels,
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(A3)):
    Ai = [x for x in A3[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 9:    
          pl.text(0.5*i-0.02,yy-1.2,str(Ai[j]),fontsize=12,zorder=10)

ax2.axes.get_xaxis().set_visible(False)
ax2.set_ylabel('number of graphs \n u = 3',rotation = 90)








#graph subplot for u = 4
A4 = makeA(3)
mycolorlistu4 = [(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), (0.6151274326753975, 0.4961389476149738, 0.15244053646953548), (0.1562085876188265, 0.44786703170340336, 0.9887241674046707), (0.4210506028639077, 0.22000131667972023, 0.37841949185273394), (0.7728656344058752, 0.47367399916287833, 0.026245548153039366), (0.904005064928743, 0.3038725882767085, 0.9399279068775889), (0.39140782566655674, 0.7613012099948101, 0.7475874114794775), (0.09653595917613811, 0.43566457484639054, 0.9375581594394308), (0.8599446540919113, 0.2080708213188862, 0.8893517695418856), (0.022700048163251885, 0.658455757390323, 0.45194508876647577), (0.12487596822954139, 0.1286185769691658, 0.6973677590395778), (0.7072265637451247, 0.795648339142106, 0.4662593453344923), (0.9522043509564118, 0.8383482335114356, 0.04624824811210648), (0.5349135197530913, 0.856298939520587, 0.4394603015585242), (0.2509444122476855, 0.7236657923769131, 0.1685356796751546), (0.4681299494331541, 0.7560613323413682, 0.10402356714939609), (0.9439367271803931, 0.9189366721892608, 0.7886855210193017), (0.6728885913928909, 0.05745471437828886, 0.572649550344611), (0.40222983289275105, 0.9345684739537153, 0.566491195073673), (0.6713347042221948, 0.44827277249822983, 0.5758028025623169), (0.2536385202352366, 0.6050891521826539, 0.20807572283377163), (0.5834926798241886, 0.9123922099176205, 0.3230169974274457), (0.2646659319053375, 0.5140308942688593, 0.6505540444073039), (0.21112416388960142, 0.7892901500348418, 0.5183165258146284), (0.4486671924545097, 0.7470804073657552, 0.5703015708258113), (0.35582076909521787, 0.8745064854695166, 0.3545516591571266), (0.561698593156714, 0.8903102946046827, 0.5464538203577384), (0.26867538636637267, 0.517149856740674, 0.6730945199483196), (0.24317906305210757, 0.07199642368662595, 0.5671977646914638), (0.47635429692725495, 0.4789345757264668, 0.0718946728096218), (0.060221542213292456, 0.01914731167580286, 0.3055281480683151), (0.16702426111200774, 0.4655359591353041, 0.719905064337108), (0.08031539146038547, 0.0017551759017343516, 0.39781039742275426), (0.9186112193751612, 0.9971574701448443, 0.4115498230749317), (0.8178399158369203, 0.4410663732902309, 0.9063118009279388), (0.36416864540171323, 0.11168129858682041, 0.3823234144296125), (0.5881225017148161, 0.3593781819535352, 0.8511807882850154), (0.6191625597266228, 0.11373098531803749, 0.21350708978657373), (0.05579287256358989, 0.8058805555166871, 0.8290616442329036), (0.8357294715419766, 0.4866366292227746, 0.7651889939570051), (0.7734425349611564, 0.804568911984321, 0.6096459159849782), (0.8247554199997241, 0.3064422458203301, 0.4216190559071715), (0.606928934759279, 0.18954053420608696, 0.3971704554820378), (0.5978156891010609, 0.5169556563023058, 0.4939556759014553), (0.13541805572209464, 0.8936966072954952, 0.8987940344436746), (0.5742286772248696, 0.7935777165822888, 0.8121186549668049), (0.3453158867373033, 0.025622901363553607, 0.04167816221321052), (0.1315940819040966, 0.6653967758039159, 0.37318965562498796), (0.001368802895914678, 0.2091975258357991, 0.6643280459958798), (0.9837298071447231, 0.7457505653068923, 0.8343307644530891), (0.160440753363575, 0.12473128790108612, 0.9119808719264978), (0.4273544210658893, 0.18416993684057925, 0.34203227262130487), (0.08719382781846197, 0.7675988748519565, 0.8076046247368227), (0.23059187176367324, 0.2657253302615584, 0.3643423610154106), (0.34804362261730915, 0.39060400413164886, 0.31499780156771373), (0.4320231702054077, 0.07210261858206857, 0.07920415400870395), (0.20981445390600095, 0.30693865142032595, 0.48997043645185046), (0.9241714458529445, 0.8143896488420276, 0.7663922292951993), (0.1885301360711723, 0.8389391807577213, 0.0755369071561598)]



ax3 = plt.subplot2grid((20,7), (10,0), rowspan = 5, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax3,
                   A4,
                   mycolorlistu4,
                   xLabels=d_labels,
                   yTicks=3,
                   widths=d_widths,
                   gap = 0.005,
                   scale=False
)

for i in range(len(A4)):
    Ai = [x for x in A4[i] if x>0]
    y = [x/2.0 for x in Ai]
    for j in range(len(Ai)):
        if j>0:
            yy = y[j]+np.sum(Ai[0:j])
        else:
            yy = y[j]    
        if int(Ai[j]) > 8:    
          pl.text(0.5*i-0.02,yy-1.2,str(Ai[j]),fontsize=12,zorder=10)

ax3.set_xticklabels(d_labels,rotation=0)
ax3.set_xlabel('densities')
ax3.set_ylabel('u = 4')










###################################LEGEND################################################

#ax4 = plt.subplot2grid((20,7), (13,2),colspan=2,rowspan = 2)
ax4 = plt.subplot2grid((20,7), (16,2),colspan=2,rowspan = 3)
bararray = [1,2,3]
eqc_labels = ['1','2','4']
my_legend_color_list = [
mycolorlistu4[0],
mycolorlistu4[1],
mycolorlistu4[2]]
ax4.bar(bararray,[.1]*3,color=my_legend_color_list,align='center')
ax4.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax4.axes.get_yaxis().set_visible(False)
ax4.set_xticklabels(eqc_labels)
ax4.set_axis_bgcolor('w')

#ax5 = plt.subplot2grid((20,7), (13,4),colspan=2,rowspan=2)
ax5 = plt.subplot2grid((20,7), (16,4),colspan=2,rowspan=3)
bararray = [4,5,6]
eqc_labels = ['999','>1000','superclique']
my_legend_color_list = [
mycolorlistu4[-3],
mycolorlistu4[-2],
mycolorlistu4[-1]]
ax5.bar(bararray,[1]*3,color=my_legend_color_list,align='center')
ax5.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax5.axes.get_yaxis().set_visible(False)
ax5.set_xticklabels(eqc_labels)
ax5.set_axis_bgcolor('w')


plt.text(3.2,0,"...")
plt.text(-3,0,"Equivalence Class Size")








plt.tight_layout()
plt.savefig('sb_nodes_6.svgz')
plt.show()