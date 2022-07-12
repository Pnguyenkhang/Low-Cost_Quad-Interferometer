#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import csv
import time
import datetime
import serial
import numpy as np
import math
import pandas as pd

# Constants
theta_value = 0
TEMP_value = 0
t = 0
init = True
total_expansion = 0
PD1_mean =1.59   # manual input before run
PD2_mean = 0.74  # manual input before run
sum_phase = 0    # Total phase change

K = (2*np.pi)/(532*10**(-9))   #wavenumber depending on wavelength of laser

fieldnames = ['PD1','PD2','TEMP','theta','expansion','time']

# Create csv file to log voltage readings of photodiodes, temperature, and calculated phase
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
# For windows, will have to find com port connection
# Connect to trinket through USB port, easiest way to find serial connection is using Adafruit Mu editor and hovering over CPU symbol on bottom right
# copy and paste USB path name into next line ***with serial.Serial('PATH NAME HERE', 19200, timeout=0.01) as ser:***
with serial.Serial('/dev/cu.usbmodem14101', 19200, timeout=0.01) as ser:
    while True:
            ct = datetime.datetime.now()
            time_start = ct.timestamp()
            
            line = ser.readline()   # read a '\n' terminated line
            
            line_list = line.split()   #make string into list
            map_object = map(float,line_list)
            values = list(map_object)  # values is a float valued list of incoming data from USB
    
            if init == True:   #initialize expansion list and set prev_theta
                prev_theta = math.atan2(values[1] - PD2_mean,values[0] - PD1_mean)
                index = 0
                delta_theta = 0
                TEMP_value = values[2]
                init = False
                    
            else:   #calculate change in phase and translate into distance flux
                if len(values) != 3:   #error checking
                    continue
                else:
                    PD1_value = values[0]
                    PD2_value = values[1]
                    TEMP_value = values[2]
                    
                    theta_value = math.atan2(values[1] - PD2_mean,values[0] - PD1_mean)
                    delta_theta = theta_value - prev_theta
                    
                    #due to arctan2() we must check direction of phase change at theta = pi or theta = -pi
                    if delta_theta > 6:
                        delta_theta = delta_theta - 2*np.pi
                    elif delta_theta < -6:
                        delta_theta = delta_theta +2*np.pi
                    prev_theta = theta_value
                    sum_phase += delta_theta
                    if sum_phase > 2*math.pi or sum_phase < -2*math.pi:   # If 2*pi phase angle reached, reset total
                        sum_phase = 0
                        data_2 = pd.read_csv('data.csv')
                        stream_1 = data_2['PD1']
                        stream_2 = data_2['PD2']
                        PD1_mean = (np.max(stream_1[-index:]) +np.min(stream_1[-index:]))/2
                        PD2_mean = (np.max(stream_2[-index:]) +np.min(stream_2[-index:]))/2
                        index = 0
                        theta_value = math.atan2(values[1] - PD2_mean,values[0] - PD1_mean)
                        
                #convert phase change to expansion
                expansion_step = delta_theta/K
                total_expansion += expansion_step
                
                #log all data into data.csv
                with open('data.csv', 'a') as csv_file:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                    info = {
                        'PD1':PD1_value,
                        'PD2':PD2_value,
                        'theta':theta_value,
                        'TEMP':TEMP_value,
                        'expansion':total_expansion,
                        'time':t
                    }
                    
                    csv_writer.writerow(info)
                    
                    index += 1
                    ct = datetime.datetime.now()
                    time_end = ct.timestamp()
                    t += (time_end - time_start)

