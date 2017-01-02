import matplotlib.pyplot as plt

#provide function definition here
def f(x):
   return (x*2) #+ 34 - (x**2)

def g(x):
   return (x*2)+20

def fillYaxis1():  ## returns list
    aList = []
    for iter in range(10):
      aList.append(f(iter))
    
    return aList

def fillYaxis2():  ## returns list
    aList = []
    for iter in range(10):
      aList.append(g(iter))
    
    return aList

def TickLabels(iList):
    oList = []
    for iter in range(len(iList)):
        oList.append(""+str(iList[iter])+"")
    
    return oList


def plotGraph():
  plt.title('x vs f(x)   \n')
  x_axis = range(10) #[1,2,3,4,5]
  x_tick_labels = TickLabels(x_axis)
  plt.xlim(min(x_axis),max(x_axis))
  plt.xticks(x_axis, x_tick_labels, rotation='horizontal' , fontsize='10')
  plt.xlabel('\n X  -- > ', fontsize=14, color='blue')
  plt.ylabel('Y  -- > \n', fontsize=14, color='blue',rotation='vertical' )
  #plt.yticks(y_axis, y_tick_labels, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  ###f(x)
  y_axis1 =  fillYaxis1()
  ###g(x)
  y_axis2 =  fillYaxis2()
  plt.ylim(min(y_axis1+y_axis2), max(y_axis1+y_axis2)) ## + concatenates the list
  y_tick_labels1 = TickLabels(y_axis1)
  y_tick_labels2 = TickLabels(y_axis2)
  ###########################################################################
  ####### 
  ###########################################################################
  y_axis_all = y_axis1+y_axis2
  y_tick_labels_ALL = y_tick_labels1+y_tick_labels2
  ###########################################################################
  ####### 
  ###########################################################################
  plt.yticks(y_axis_all, y_tick_labels_ALL, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  line1, = plt.plot(x_axis,y_axis1,linestyle = "-", color = "b", marker = "d", markerfacecolor = "b", markersize=10) 
  line2, = plt.plot(x_axis,y_axis2,linestyle = "-", color = "g", marker = "d", markerfacecolor = "g", markersize=10)
  #plt.grid(True, which ="major")
  #plt.grid(True, which ="minor")
  ax = plt.axes()
  ax.yaxis.grid(True)
  plt.legend((line1,line2),("f(x) = (x*2)","g(x) = (x*2)+20"),loc="upper left")
  plt.show()

plotGraph()

