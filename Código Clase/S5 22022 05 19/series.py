# -*- coding: utf-8 -*-
"""
# ******** SEMANA 5 ***********
Created on Thu May 19 09:10:25 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""


# from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt 

# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

# import matplotlib.pyplot as plt 
# x=[0,10,20,30,60,90]
# y=[-4.39,-4.69,-4.99,-5.30,-6.21,-7.13]
# fig=plt.figure()
# ax=fig.add_axes([0,0,1,1]) #grand
# plt.plot(x,y)
# plt.show()

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(data["calories"])
print(df.loc["day2"])
df = pd.DataFrame(data)  #si dejo la definición de arrriba no corre 
print(df.loc[1][0])