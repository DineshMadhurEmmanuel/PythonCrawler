# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:00:44 2023

@author: DINESHCH
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('mpg.csv')
df1 = df[['mpg','cylinders','origin','model_year']]
df1.head()
df1
df.groupby('model_year').mean(numeric_only=True)


"""
If you got a similar TypeError after a groupby operation 
(e.g. TypeError: Could not convert ace to numeric), 
then you probably have pandas>=2.0.
groupby.mean() has numeric_only= argument whose 
default value was True in the past but since pandas 2.0, 
its default value is False. An implication is that string columns are not dropped 
when a statistical method such as mean or std is called on the groupby object 
(as was done in the past). To solve the issue, pass numeric_only=True.

"""

