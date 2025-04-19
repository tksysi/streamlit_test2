import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


# 描画エリアを設定
# ax = fig.add_axes([0.2, 0.2, 0.7, 0.7], projection='3d')
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# アニメを描写するプレースホルダーを作成
placeholder = st.empty()

Ey = 1.0
Ez = 1.5
theta_deg = -60.0

theta = theta_deg * np.pi / 180.0
dt = np.pi/20
t = np.arange(0, 2*np.pi, dt)
xx = np.arange(0, 10*np.pi, np.pi/20)    

n = 0
while (True):
    x = xx[n%len(xx)]
    y = 0
    z = 0
    u = 0
    v = Ey * np.cos(x)
    w = Ez * np.cos(x - theta)
    l = np.sqrt(u**2 + v**2 + w**2)

    x2 = xx[0:n%len(xx)+1]
    y2 = Ey * np.cos(x2)
    z2 = Ez * np.cos(x2 - theta)
        
    ax.cla()
    ax.quiver(x, y, z, u, v, w, length=1, pivot='tail', arrow_length_ratio=0.2)
    ax.plot(x2, y2, z2)
    ax.plot(xx, np.zeros(len(xx)), np.zeros(len(xx)), 'k')
    ax.set_xlim(0, np.max(xx))
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    elev = 30
    azim = -40
    ax.view_init(elev=elev, azim=azim)

    placeholder.pyplot(fig)

    n += 1