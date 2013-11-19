##############################################################
# Tiffany Hall
# OCNG 689 Homework 3
# Using a NetCDF file, create  a map and time series
# Input: NetCDF file
# Output: 1.) Simple map and 2.) a time series graph
# Packages used: Basemap, Numpy, Pyplot, NetCDF4, and Pandas
############################################################## 

from mpl_toolkits.basemap import Basemap
import netCDF4
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Pulling out the variables
nc = netCDF4.Dataset("http://apdrc.soest.hawaii.edu/dods/public_data/Interpolated_precipitation/cpc_rainfall/1.0deg")
rain = nc.variables['rain'][0,0,:,:]
lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]

#Creating a grid
lon, lat = np.meshgrid(lon, lat)
m = Basemap(llcrnrlon=0,llcrnrlat=-90,urcrnrlon=360,urcrnrlat=90,projection='robin',lon_0=180)
x,y = m(lon, lat) 

# Drawing basic map
fig = plt.figure()
m.drawcoastlines(linewidth = 1.0)
m.drawparallels(np.arange(-90.,90.,15.), labels =[1,0,0,1],fontsize=8)
m.drawmeridians(np.arange(-180.,181.,40.),labels =[0,1,0,1],fontsize=8)
m.drawmapboundary()

# Placing the data over the map
plt.contourf(x,y,rain,cmap = plt.cm.RdBu_r)
plt.contourf(x,y,rain,np.arange(-1,1.2,0.02),  cmap = plt.cm.RdBu_r)
cb = plt.colorbar(orientation='horizontal')
plt.title('Monthly Mean Rainfall Amount', fontsize =16 , style ='italic')
plt.show()


# Part 2: making pandas timeseries 

#setting up time for timeseries 
time = nc.variables['time']
rain_ts = nc.variables['rain'][:,0, 100, 100] # check out the shape first. Then select an x(100) and y(100) in the shape for the series
dates = netCDF4.num2date(time[:],time.units)
timeseries = pd.Series(rain_ts,index=dates)
data_frame = pd.DataFrame(timeseries)

#plotting pandas timeseries 
data_frame.plot(figsize=(25.0,5.0),color="purple",legend=False)
plt.title('Monthly Mean Rainfall Amount')
plt.xlabel("Month")
plt.ylabel("Monthly Mean Rainfall (unit=0.1 mm/day)")
plt.show()
plt.savefig('Rainfall_timeseries_Hw3.png')