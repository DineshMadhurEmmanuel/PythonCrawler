# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:01:57 2023

@author: DINESHCH
"""

import numpy as np
import pandas as pd

"""
dict1 = {"brazil":100,"Uganda":200, "USA":400}
dict2 = {"brazil":30,"Japan":20, "ElSal":40}
Q1 =  pd.Series(dict1)
Q2 =  pd.Series(dict2)
Q1.add(Q2,fill_value=100)
"""
"""
def lastfour(num):
    return str(num)[-4:] 


df = pd.read_csv("tips.csv")
df
df.info()
df.describe()
df['CC Number'][0]
lastfour(df['CC Number'][0])

df['last_four'] = df['CC Number'].apply(lastfour)
df
"""

d = {'A':[1,2,3], 'B':[4,5,6]}

df1 = pd.DataFrame(data=d)
df1

"""
def fxy(x,y):
    return x*y

df1['function_Multiple'] = df1.apply(lambda x : fxy(df1['A'],df1['B']),axis = 1)


"""

import numpy as np
import pandas as pd

d = {'A':(1,2,3), 'B':(4,5,6)}

df1 = pd.DataFrame(data=d)
df1

def fxy(x,y):
    return x*y

#df1['function_Multiple'] = df1.apply(fxy ,axis = 1)

df1['FuncMultiple'] = np.vectorize (fxy)(df1['A'],df1['B'])
df1['func'] = np.multiply(df1['A'],df1['B'])
df1



















