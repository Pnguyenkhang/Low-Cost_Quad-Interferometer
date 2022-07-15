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
    plt.plot(x,y3)   #change y3 to y2 for plotting temperature vs time
    
  
    plt.xlabel('time (s)')
    plt.ylabel('Expansion (m)')

ani = matplotlib.animation.FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


# In[ ]:




