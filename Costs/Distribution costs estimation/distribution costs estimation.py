#distribution cost estimation. For further detail, check the report on this directory
import pandas as pd
import numpy as np
dfs=pd.read_csv("tables/categorized counties.csv")
'''The calculations of each of the distribution cost estimates 
is made using a simplified version of the formulas contained in the report
for improving performance and for asuring none of our variables becomes cero (as some of them are really small)'''
for c in dfs.index.tolist():
    dfs.set_value(c,"DistributionCost2 (millions of MXN)", dfs.loc[c,"Real state with electricity"].astype("int64")*1922*21172.83/(3*dfs["Real state with electricity"].astype('int64').sum())+dfs.loc[c,"land area (km^2)"].astype("int64")*21172.83/(dfs["land area (km^2)"].astype('int64').sum()*3))

    if str(dfs.loc[c,'County type'])=="urban":
        dfs.set_value(c,'DistributionCost1 (millions of MXN)',dfs.loc[c,'land area (km^2)'].astype("float64")*1*dfs.loc[c,"Real state with electricity"].astype("int64")*.05*.05 + dfs.loc[c,"Real state with electricity"].astype("int64")/8 * .35)
    else:
        dfs.set_value(c,'DistributionCost1 (millions of MXN)',dfs.loc[c,'land area (km^2)'].astype("float64")*2*dfs.loc[c,"Real state with electricity"].astype("int64")*.1*.003 + dfs.loc[c,"Real state with electricity"].astype("int64")/6 *.45)
    dfs.set_value(c,"diference of estimation (millions of MXN)",abs(dfs.loc[c,'DistributionCost1 (millions of MXN)']-dfs.loc[c,"DistributionCost2 (millions of MXN)"]))
dfs.to_csv("tables/categorized counties.csv",index=False)