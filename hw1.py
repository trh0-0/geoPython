#Tiffany Hall
#OCNG 689
#HW 1 Pt1: Initial code
#9/12/13

f = open('C:\\Users\\Tiffany\\Desktop\\view_text_file.txt')
import numpy as np
from datetime import datetime

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
print 'Wind Speed is ',u
print 'Wind Direction is ', v



