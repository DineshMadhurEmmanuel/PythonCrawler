# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

"""
Created on Thu Sep 14 22:15:23 2023

@author: DINESHCH
"""

"""

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,10)
y=x*2
plt.plot(x,y)
plt.xlim(1,6)
plt.savefig('test')

"""
"""
x=np.linspace(10,20,12,endpoint=True,dtype=int,axis=0)
#print(x)
y=x ** 4
fig = plt.figure()
fig.xlim(0,100)
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
#plt.show()

"""
x=np.arange(10)
y=np.arange(10,20)

fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(12,8),dpi=60)
axes[0][0].plot(x,y)
fig.suptitle('Title')
axes[0][0].set_title('subplot title')
#fig.tight_layout()
plt.tight_layout()
fig.savefig('subplot.png',bbox_inches='tight')


"""
axes.plot(x,y)
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Title')#;

"""