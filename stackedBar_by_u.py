#this code is specifically used for plotting
#a stacked bar plot for the zickle file 'saturn_nodes_5_density_0.25_ral_UMAX_11_.zkl'
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


UMAX = 10
l = 'mars_nodes_5_density_0.25_UMAX_11_ral_.zkl'
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
  print "u:",U+1
  print "c:",c
  print "\n"
  return c

#dc is a dictionary where key = u being considered and value = dictionary of equivalence class sizes
#usz is a set of all equivalence class sizes(not frequencies)
d = zkl.load(l) 
usz = set()
dc = {}
for u in range(UMAX):
    dc[u] = get_counts(d,u+1)
    for v in dc[u]:
        usz.add(v)

print usz
#adding all seen equivalence sizes for every density
for u in range(UMAX):
    for c in usz:
        if not c in dc[u]:
            dc[u][c] = 0

#A is all eqc frequencies for all density from bottom to top 
A = []
for u in range(UMAX):
    A.append([dc[u][x] for x in np.sort(dc[u].keys())])

  
d_widths = [.5]*UMAX
d_labels = []
for u in range(UMAX):
    d_labels.append(str(u+2))

#if wanting to generate a random list of colors
#my_color_list = []
#for i in range(len(usz)):
#	my_color_list.append((random.random(),random.random(),random.random()))
#print "mycolorlist",my_color_list

#these colors seem to work well
my_color_list = [(0.9769448735268946, 0.6468696110452877, 0.2151452804329661), (0.37645505989354233, 0.6875228836084111, 0.30496111115768654), (0.6151274326753975, 0.4961389476149738, 0.15244053646953548), (0.1562085876188265, 0.44786703170340336, 0.9887241674046707), (0.4210506028639077, 0.22000131667972023, 0.37841949185273394), (0.7728656344058752, 0.47367399916287833, 0.026245548153039366), (0.904005064928743, 0.3038725882767085, 0.9399279068775889), (0.09653595917613811, 0.43566457484639054, 0.9375581594394308), (0.5934259725250017, 0.6259544064286037, 0.8943937276483482), (0.1834548561930609, 0.8625908063396674, 0.2808367027257399), (0.9522043509564118, 0.8383482335114356, 0.04624824811210648), (0.2509444122476855, 0.7236657923769131, 0.1685356796751546), (0.4681299494331541, 0.7560613323413682, 0.10402356714939609), (0.9439367271803931, 0.9189366721892608, 0.7886855210193017), (0.6980608691309792, 0.6296583577840691, 0.10122715703511265), (0.7530798564980008, 0.14571022694658842, 0.1558625362484024), (0.2646659319053375, 0.5140308942688593, 0.6505540444073039), (0.32532392896062434, 0.6771986595824758, 0.6804464385760941), (0.561698593156714, 0.8903102946046827, 0.5464538203577384), (0.06195801226204156, 0.4085195670330185, 0.16777660887869106), (0.4862983226162474, 0.9266576030195525, 0.5200207123141651), (0.8823494781169269, 0.8602854575796756, 0.46655973657031047), (0.060221542213292456, 0.01914731167580286, 0.3055281480683151), (0.766342531208258, 0.9245825374766737, 0.37031711910405163), (0.8918452889529781, 0.3489446890522606, 0.5363393265500108), (0.39140968224876604, 0.20490073625104321, 0.49724364222766826), (0.15440849286794844, 0.5109256317494821, 0.918663018768346), (0.46426804376009356, 0.5040025154668996, 0.18863898344256602), (0.6418660472107188, 0.19387172503903427, 0.08253445229983347), (0.31722667708720487, 0.441657298575016, 0.7178566635952561), (0.606928934759279, 0.18954053420608696, 0.3971704554820378), (0.4417364105098468, 0.4369407216947674, 0.16241194628082245), (0.8107807623400896, 0.3099877573648637, 0.435731436486533), (0.2329089726116761, 0.10130531525410325, 0.5097643277292452), (0.5665782970092119, 0.22826862385734814, 0.38958016270033535), (0.48137410722891594, 0.09467528600649266, 0.5375593747271779), (0.09726368948435926, 0.8369969882905206, 0.07986516857033343), (0.2694751359724161, 0.45498770799919086, 0.6448059472136883), (0.38997444066817866, 0.9781779063852679, 0.874217562859495), (0.7051477513703358, 0.5702924839652445, 0.24312377606293833), (0.5709641799914025, 0.743539099020067, 0.8261827299024898), (0.8178345478004484, 0.981435239104708, 0.6544046775407857), (0.4320231702054077, 0.07210261858206857, 0.07920415400870395), (0.5627424217341767, 0.1968727734442548, 0.3595950676513303), (0.20981445390600095, 0.30693865142032595, 0.48997043645185046), (0.9241714458529445, 0.8143896488420276, 0.7663922292951993), (0.1885301360711723, 0.8389391807577213, 0.0755369071561598)]


############################################################################################
ax1 = plt.subplot2grid((7,7), (0,0), rowspan = 6, colspan=7)
SBG = StackedBarGrapher()
SBG.stackedBarPlot(ax1,
                   A,
                   my_color_list,
                   xLabels=d_labels,
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
        if int(Ai[j]) > 5:    
          pl.text(0.5*i-0.02,yy-1.2,str(Ai[j]),fontsize=12,zorder=10)

ax1.set_xticklabels(d_labels,rotation=0)
ax1.set_xlabel('undersampling rate (u)')
ax1.set_ylabel('number of graphs')
ax1.set_title('n = 5, number of graphs per u = 100,density=25%',multialignment='center')


###################################################################################
#helpful note:
#a(0)
#a+1
#a+2
#b(0) #b+1 #b+2
#the whole thing is divided into c by d blocks
#plt.subplot2grid((c,d), (a, b),rowspan = e, colspan = f)

ax2 = plt.subplot2grid((7,7), (6,1),rowspan =1,colspan=3)
bararray = [1,2,3]
eqc_labels = ['1','2','4']
my_legend_color_list = [
my_color_list[0],
my_color_list[1],
my_color_list[2]]
ax2.bar(bararray,[1]*3,color=my_legend_color_list,align='center')
ax2.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax2.axes.get_yaxis().set_visible(False)
ax2.set_xticklabels(eqc_labels)
ax2.set_axis_bgcolor('w')



######################################################################
ax3 = plt.subplot2grid((7,7), (6,4),rowspan =1,colspan=3)
bararray = [4,5,6]
eqc_labels = ['999','>1000','superclique']
my_legend_color_list = [
my_color_list[-3],
my_color_list[-2],
my_color_list[-1]]
ax3.bar(bararray,[1]*3,color=my_legend_color_list,align='center')
ax3.set_xticks(np.arange(min(bararray), max(bararray)+1, 1.0))
ax3.axes.get_yaxis().set_visible(False)
ax3.set_xticklabels(eqc_labels)
ax3.set_axis_bgcolor('w')





plt.text(3.35,0,"...")
plt.text(-1,-1,"Equivalence \n Class Size")
plt.tight_layout()
plt.savefig('sb_nodes_5_density_.25_UMAX_11.svgz')
plt.show()



