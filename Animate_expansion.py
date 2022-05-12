#!/usr/bin/env python
# coding: utf-8

# In[8]:


from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('fivethirtyeight')


# In[14]:


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['time']
    y1 = data['theta']
    y2 = data['TEMP']
    y3 = data['expansion']
    
    plt.cla()
    '''
    if len(x) > 10000:
        plt.plot(x[-10000:],y1[-10000:])
        #plt.plot(x[-10000:],y2[-10000:])
        #plt.plot(x[-10000:],y3[-10000:])
    else:
        plt.plot(x,y2)
    '''
    plt.plot(x,y3)
    
  
    #plt.xlabel('PD1')
    #plt.ylabel('PD2')

ani = matplotlib.animation.FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


# In[ ]:




