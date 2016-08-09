import pandas as pd
import csv
import os




import pandas as pd
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
import matplotlib as mpl

import numpy as np
import datetime as dt
import sys







content = os.listdir("../Data/Production-Drought-Precipitation") # returns list
printG = "Planta,25%,50%,75%,Year25%,Year50%,Year75%"

def historical():
    with open(r"capacityFactor.csv", "wb") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(printG)
        for element in content:

            ent = os.listdir("../Data/Production/%s"%element)
            for en in ent:
                print en
                try:
                    data = pd.read_csv("../Data/Production/%s/%s"%(element,en),index_col=0)
                    # dato = str(data.columns.values[0])
                    # data[data == 0] = None
                    # qs, bins = pd.qcut(data,[.25, .5, .75], retbins=True)
                    # print bins[0], bins[1],bins[2]
                    # dfList = data[dato].tolist()
                    # dato0 = min(dfList, key=lambda x:abs(x-bins[0]))
                    # dato1 = min(dfList, key=lambda x:abs(x-bins[1]))
                    # dato2 = min(dfList, key=lambda x:abs(x-bins[2]))
                    # dato0 = data[data[dato] == dato0].index.tolist()
                    # dato1 = data[data[dato] == dato1].index.tolist()
                    # dato2 = data[data[dato] == dato2].index.tolist()
                    # print dato0, dato1, dato2
                    # #print pd.Series(bins, index=['Production_25', 'Production_50', 'Production_75'])
                    # row = str(en[:len(en)-4])+","+str(bins[0])+","+str(bins[1])+","+str(bins[2])+","+str(dato0[0][:4])+","+str(dato1[0][:4])+","+str(dato2[0][:4])
                    # spamwriter.writerow([row])
                except (ValueError, IndexError):
                    pass






def annual():
    with open(r"capacityFactorAD.csv", "wb") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                             quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(printG)
        for element in content:
            ent = os.listdir("../Data/Production/%s"%element)
            for en in ent:
                #print en
                try:
                    lista= []
                    for i in range(0,120,12):
                        data = pd.read_csv("../Data/Production/%s/%s"%(element,en),index_col=0)
                        data =  data[i:i+12]
                        column = data.columns.values[0]
                        lista.append(data[column].mean())
                    years =['2006', '2007', '2008', '2009','2010', '2011', '2012', '2013','2014', '2015']
                    data = pd.DataFrame({'year':years, 'Production-Ave':lista})
                    d= data['Production-Ave']
                    qs, bins = pd.qcut(d,[.25, .5, .75], retbins=True)
                    dfList = data['Production-Ave'].tolist()
                    dato0 = min(dfList, key=lambda x:abs(x-bins[0]))
                    dato1 = min(dfList, key=lambda x:abs(x-bins[1]))
                    dato2 = min(dfList, key=lambda x:abs(x-bins[2]))
                    dato0 = data[data['Production-Ave'] == dato0].index.tolist()
                    year0 = data.loc[dato0]
                    year0 = year0.year.values[0]
                    dato1 = data[data['Production-Ave'] == dato1].index.tolist()
                    year1 = data.loc[dato1]
                    year1 = year1.year.values[0]
                    dato2 = data[data['Production-Ave'] == dato2].index.tolist()
                    year2 = data.loc[dato2]
                    year2 = year2.year.values[0]
                    #print str(en[:len(en)-4])+","+str(bins[0])+","+str(bins[1])+","+str(bins[2])+","+str(year0)+","+str(year1)+","+str(year2)
                    row = str(en[:len(en)-4])+","+str(bins[0])+","+str(bins[1])+","+str(bins[2])+","+str(year0)+","+str(year1)+","+str(year2)
                    spamwriter.writerow([row])
                except (ValueError, IndexError):
                    pass


def plotC(element,en):
    lista = []
    for i in range(0,120,12):
        data = pd.read_csv("../Data/Production/%s/%s.csv"%(element,en),index_col=0)
        data =  data[i:i+12]
        column = data.columns.values[0]
        lista.append(data[column].mean())
    years =['2006', '2007', '2008', '2009','2010', '2011', '2012', '2013','2014', '2015']
    data = pd.DataFrame({'year':years, 'Production-Ave':lista})

    d= data['Production-Ave']
    #print d
    qs, bins = pd.qcut(d,[.25, .5, .75], retbins=True)

    print data.columns.values[0]
    fig, ax = plt.subplots()
    fig.canvas.draw()
    years =['2006', '2007', '2008', '2009','2010', '2011', '2012', '2013','2014', '2015']
    ax.set_xticklabels(years)
    plt.plot(years, data[data.columns.values[0]], marker='o', linestyle='-')
    plt.axhline(y=bins[0],linestyle='--', color='g', label="25%")
    plt.axhline(y=bins[1],linestyle='--', color='c', label="50%")
    plt.axhline(y=bins[2],linestyle='--', color='m', label="75%")
    plt.xlabel('Time')
    plt.ylabel('Net Generation [MW/h]')
    plt.title('Net Generation')
    plt.legend()
    plt.show()




plotC(sys.argv[1],sys.argv[2])
annual()