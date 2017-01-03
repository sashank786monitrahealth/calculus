from __future__ import division
import matplotlib.pyplot as plt

#provide function definition here
def f(x):
   return (x**2) #+ 34 - (x**2)

def g(x):
   return (x**2)+20

def fillYaxis1(xList):  ## returns list
    aList = []
    for iter in range(len(xList)):
      aList.append(f(xList[iter]))
    
    return aList

def fillYaxis2(xList, yList):  ## pass data points of x and y returns list of slope
    aList = []
    prevX =0
    prevY =0
    slope =0
    for iter in range(len(xList)):
      if iter == 0:
         #aList.append(slope)
         prevX =xList[iter]
         prevY =yList[iter]
      else:
         slope = round((yList[iter]-prevY)/(xList[iter]-prevX),2) ##slope = (y2-y1)/(x2-x1)
         aList.append(slope)
         prevX =xList[iter]
         prevY =yList[iter]
    
    aList.append(slope)
    return aList

def TickLabels(iList):
    oList = []
    for iter in range(len(iList)):
        oList.append(""+str(iList[iter])+"")
    
    return oList


def plotGraph():
  plt.title('x vs f(x)   \n')
  x_axis = range(10+1) #[1,2,3,4,5]
  x_tick_labels = TickLabels(x_axis)
  plt.xlim(x_axis[0],x_axis[-2])
  plt.xticks(x_axis[0:-1], x_tick_labels[0:-1], rotation='horizontal' , fontsize='10')
  plt.xlabel('\n X  -- > ', fontsize=14, color='blue')
  plt.ylabel('Y  -- > \n', fontsize=14, color='blue',rotation='vertical' )
  #plt.yticks(y_axis, y_tick_labels, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  ###f(x)
  y_axis1 =  fillYaxis1(x_axis)
  ###g(x)
  y_axis2 =  fillYaxis2(x_axis,y_axis1)
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
  ax.xaxis.grid(True)
  plt.legend((line1,line2),("f(x) = (x^2)","g(x) = slope of f(x)"),loc="upper left")
  plt.show()

plotGraph()

