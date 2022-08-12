import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from math import pi as pi 
fileName = input()
data_ = pd.read_csv(fileName) 

cols = ["N(MN0:GM)","N(MN0:VTH)","N(MN0:CGD)","N(MN0:CGS)","N(MN0:GDS)","I(VD)","VG"]

gm = data_[[cols[0]]].to_numpy()
vth = data_[[cols[1]]].to_numpy()
cgd = -1*data_[[cols[2]]].to_numpy()
cgs = -1*data_[[cols[3]]].to_numpy()
gds = data_[[cols[4]]].to_numpy()
id = -1*data_[[cols[5]]].to_numpy()
vgs = data_[[cols[6]]].to_numpy() 
cgg = cgs + cgd 

vov = vgs - vth 
gmro = gm/gds 
ft = 1/(2*pi*cgg)
gmid = gm/id 
ft_gmid = ft*gmid 


plt.plot(vgs,gmro)
plt.show()