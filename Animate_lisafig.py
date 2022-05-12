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
    y1 = data['PD1']
    y2 = data['PD2']
    
    plt.cla()
    if len(x) > 10000:
        plt.plot(y1[-50000:],y2[-50000:], label = 'PD1')
        plt.plot(y1[-15:-1],y2[-15:-1],'r')
        
    else:
    	plt.plot(y1,y2, label = 'PD1')
    	plt.plot(y1[-15:-1],y2[-15:-1],'r')
        
        
  
    plt.xlabel('voltage (V)')
    plt.ylabel('voltage (V)')
    #plt.xlim(0.15,0.3)
    #plt.ylim(0.2,0.3)

ani = matplotlib.animation.FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()




# In[ ]:




