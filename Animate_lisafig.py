#!/usr/bin/env python
# coding: utf-8

from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('fivethirtyeight')

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
        
        
  
    plt.xlabel('PD_A voltage (V)')
    plt.ylabel('PD_B voltage (V)')

ani = matplotlib.animation.FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
