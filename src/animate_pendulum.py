# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:52:54 2026

@author: Ebiringa
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Import solved numerical data from simulate_pendulum
from simulate_pendulum import sol, parameters

#Extract solution angle and time points
th1_vals = sol.y[0]
th2_vals = sol.y[2]
t_vals = sol.t

#Extract parameters
g_val, m1_val, m2_val, l1_val, l2_val = parameters

#Convert angles to cartesian coordinates (x, y)
x1 = l1_val*np.sin(th1_vals)
y1 = -l1_val*np.cos(th1_vals)

x2 = x1 + l2_val*np.sin(th2_vals)
y2 = y1 - l2_val*np.cos(th2_vals)

#Set up Figure and axes for Animation
fig, ax = plt.subplots(figsize=(6,6))
max_length = l1_val + l2_val + 0.2
ax.set_xlim(-max_length, max_length)
ax.set_ylim(-max_length, max_length)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Double Pendulum Simulation")

#Plot elements: rods (line), bobs (dots), trail (line)
line, = ax.plot([], [], 'o-', lw=2, color='navy', markersize=8)
trail, = ax.plot([], [], '-', lw=1, color='crimson', alpha=0.6)

#Trace trail buffer (stores recent positions of mass 2)
trail_len = 150

def init():
    line.set_data([], [])
    trail.set_data([], [])
    return line, trail

def update(frame):
    #Current positions
    thisx = [0, x1[frame], x2[frame]]
    thisy = [0, y1[frame], y2[frame]]
    line.set_data(thisx, thisy)
    
    #Pendulum trail for mass 2
    start_frame = max(0, frame - trail_len)
    trail.set_data(x2[start_frame:frame], y2[start_frame:frame])
    
    return line, trail

#Run Animation
#Reduce frames and set blit=False for clean rendering
frame_step = 3
frames_to_render = range(0, len(t_vals), frame_step)
ani = FuncAnimation(fig, update, frames=frames_to_render, init_func=init, interval=20, blit=False)

print("Generating double_pendulum.gif, Please wait a moment")

ani.save("double_pendulum.gif", writer="pillow", fps=30)
print("Done")

plt.show()



















