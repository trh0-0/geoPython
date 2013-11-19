#Tiffany Hall
#OCNG 689
#HW 1 Pt3:Class
#9/12/13

import numpy as np
from datetime import datetime
from matplotlib.pyplot import *

class burl1_2011():
    def __init__(self, datafile):
        self.datafile = datafile
        f = open(self.datafile) 
        dates = []
        windir = []
        windsp = []
        pressure = []
        for line in f.readlines()[2:]:
            data = line.split()
            year = int(data[0])
            month = int(data[1])
            day = int(data[2])
            hour = int(data[3]) 
            minute = int(data[4]) 
            windir.append(float(data[5]))
            windsp.append(float(data[6]))
            pressure.append(float(data[12]))
            dates.append( datetime(year, month, day, hour, minute) )

        dates = np.array(dates) 
        pressure =np.array(pressure)
        wind_speed = np.array(windsp)
        wind_direction = np.array(windir)
        u = -wind_speed*(np.sin (wind_direction*np.pi/180))
        v = -wind_speed*(np.cos (wind_direction*np.pi/180))
        self.pressure =pressure
        self.dates = dates
        self.u = u
        self.v = v

d11= burl1_2011( 'C:\\Users\\Tiffany\\Desktop\\view_text_file.txt')
print d11.u.mean()  

y = np.sqrt(d11.u**2 + d11.v**2)

plot(d11.dates, y)
show()