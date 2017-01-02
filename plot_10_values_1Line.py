import matplotlib.pyplot as plt

#provide function definition here
def f(x):
   return (2*x) #+ 34 - (x**2)

def fillYaxis():  ## returns list
    aList = []
    for iter in range(10):
      aList.append(f(iter))
    
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
  plt.ylabel('Y -- f(X) -- > \n', fontsize=14, color='blue',rotation='vertical' )
  #plt.yticks(y_axis, y_tick_labels, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  ###f(x)
  y_axis1 =  fillYaxis()
  plt.ylim(min(y_axis1), max(y_axis1))
  y_tick_labels1 = TickLabels(y_axis1)
  ###########################################################################
  ####### 
  ###########################################################################
  y_axis_all = y_axis1
  y_tick_labels_ALL = y_tick_labels1
  ###########################################################################
  ####### 
  ###########################################################################
  plt.yticks(y_axis_all, y_tick_labels_ALL, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  line1, = plt.plot(x_axis,y_axis1,linestyle = "-", color = "#009900", marker = "d", markerfacecolor = "#009900", markersize=10) 
  #plt.grid(True, which ="major")
  #plt.grid(True, which ="minor")
  ax = plt.axes()
  ax.yaxis.grid(True)
  #plt.legend(("f(x)",loc="lower center")
  plt.show()

plotGraph()
