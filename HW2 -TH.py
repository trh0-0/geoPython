###########################
# Tiffany Hall
# OCNG 689 Lab 2
# Input - Online text file
# Output - Plot showing Daily discharge, annual average discharge for each day 
# for at least 3 decades and the standard deviation of the average of the selected site. 
##########################

import urllib
from datetime import date 
import numpy as np
import matplotlib.pyplot as plt
   
htdata = urllib.urlopen('http://waterdata.usgs.gov/ny/nwis/dv?cb_00060=on&format=rdb&period=&begin_date=1943-10-01&end_date=2013-10-14&site_no=01304000&referred_module=sw')

# Select the desired year
ch_year = 2011

dates = []
discharge = []
    
for line in htdata.readlines()[28:]:   #why is line only "USGS    01304000        2013-10-14      32      P" last line
    #print line
    data = line.split()
    if len(data) < 4:
        continue
    datesplit = data[2].split('-')
    year  = int(datesplit[0])    #why is it only reading 2013?
    month = int(datesplit[1])
    day   = int(datesplit[2])
    dates.append(date(year, month, day))      #dates begin at 1943
    try:
        q = int(data[3])    #There is missing data in this set in the discharge column
    except:                # This iterates over it and labels it nan
        q = np.nan
    discharge.append(float(q))
        
htdata.close()

# Creating arrays
dates = np.array (dates)
discharge = np.array(discharge)
days   = np.array ([d.day for d in dates])      # only counting 1-14
average = []
stdev = []
upstd = []
lowstd =[]

# Converting cubic feet per second to SI units
discharge = discharge / 35.315                   #must be in an array to be able to manipulate it

stdev = np.array(stdev)

#Selecting the time period to be looked at
months = [d.month for d in dates] 
months = np.array(months)
for month in np.unique(months):                     # month is only 10 but unique months is 1-12
    st_year = date(ch_year, 1, 1)                    
    end_year = date(ch_year+1, 1, 1)                # Makes it so that it is only a year. stops on the 1st of the next year.
    time_prd = dates[(dates>=st_year) & (dates<end_year)]
    calc_discharge = discharge[(dates>=st_year) & (dates<end_year)]  # Array ofdischages with 70 elements
    average = (np.mean(calc_discharge))             # 1 element. How to turn into more? 
    stdev = (np.std (calc_discharge))               # 1 element

# Select the time span for plotting
idx         = np.where (ch_year)
plt_dates   = dates [idx]
plt_flow    = discharge [idx]
plt_avgflow = average [idx]
plt_upstdv  = average [idx] + stdev
plt_lowstdv = average [idx] - stdev

# Plotting results
fig=plt.figure(figsize=(17,8))
fig.autofmt_xdate()

#Creating Axis
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(plt_dates, calc_discharge, color = '#000000', label = "Daily Discharge",  lw = 1)       # daily discharge
ax.plot(plt_dates, average, color = '#ff6600', label = "Annual Mean Discharge", lw = 1)    # annual discharge
ax.plot(plt_dates, plt_upstdv, ':', color = '#003300', label = 'Upper Std. Dev.')             # high standard deviation
ax.plot(plt_dates, plt_lowstdv, ':', color = '#003300', label = 'Lower Std. Dev.')            # low standard deviation
ax.fill_between(discharge, plt_upstdv, plt_lowstdv, facecolor='#ccff99',alpha=0.3)                # fill between stdev's

# Labels
plt.title('Timeseries of Discharge from 1945 to 1975 for USGS Site NO. 01304000 - NISSEQUOGUE RIVER NEAR SMITHTOWN NY', size=16)
plt.xlabel('\nDates', size= 14)
plt.ylabel(r'Discharge (m$^{3}$ s$^{-1}$)', size= 14)

#Create a legend
ax.legend()

plt.show()

# Save the output figure as a .pdf file with a dpi of 300
plt.savefig('HW2-Tiffany_Hall.png', dpi=300)

plt.close()

