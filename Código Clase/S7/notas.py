# -*- coding: utf-8 -*-
"""
# ******** SEMANA 3 ***********
Created on Fri Jun  3 19:21:07 2022
#  
# Diego Iván Oliveros Acosta @scalapp.co   @author: ITOS
# 
# [name]   []
# =============================================================================
# 
# =============================================================================
"""

import pandas as pd
data = {'name':['michael','louis','jack','jasmine'],
        'grades':[30,70,40,80],
        'result':['N/A','N/A','N/A','N/A']}

df = pd.DataFrame(data,columns=['name','grades','result'])

df.loc[df.grades>50,'result']='success'

df.loc[df.grades<50,'result']='fail'

print(df)