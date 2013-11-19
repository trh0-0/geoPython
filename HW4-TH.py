#######################################
# Tiffany Hall OCNG 689 Lab 4
#
# Create a function that returns a matplotlib colormap based on the colors provided by the specified site.
# Pick any colormap from this site (or better, have your function be flexible enough to pick any), 
# and convert it to a matplotlib colormap.
#########################################
 
import matplotlib.pyplot as plt
import matplotlib.colors as col
import urllib
import numpy as np

def Color_map(color_name):
     
    data = urllib.urlopen('http://geography.uoregon.edu/datagraphics/color/'+ color_name)
    
    # Create lists
    red = []
    green = []
    blue  =[]
    
    # Read the table and fill the lists
    for line in data.readlines()[2:]:
        colortable = line.split()
        red.append(float(colortable[0]))
        green.append(float(colortable[1]))
        blue.append(float(colortable[2]))
    
    # fitting color values into the lists
    ''' Initialize variable n as a float to use. Define the x(color index), 
    y0 (color left of x), and y1(color right of x). Fit the color values into the list by -1'''  
    r_len = len(red)
    reds = [(float(n)/ (r_len -1),red[n-1],red[n]) for n in range (r_len)]   
    greens = [(float(n)/(r_len-1),green[n-1],green[n]) for n in range (r_len)] 
    blues = [(float(n)/(r_len -1),blue[n-1],blue[n]) for n in range (r_len)] 
    
    # Put these into a dictionary
    colors_dict = {'red':reds, 'green':greens, 'blue':blues}
   
    cmap1 = col.LinearSegmentedColormap('my_colormap',colors_dict,N=256,gamma=0.75)
     
    # Plot the output
    plt.pcolor(np.random.rand(10,10),cmap= cmap1)
    plt.colorbar()
    plt.show()
    plt.savefig('my_color_map.pdf')
    
Color_map('GrMg_16.txt')


    
    
    
        
    
        
        