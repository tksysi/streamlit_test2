import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


t = st.sidebar.number_input('wavelength', 1.00000, 10.0, 1.55, step=0.0001, format="%0.4f")
i = st.sidebar.number_input('order', 0, 10, 0)
pol = st.sidebar.selectbox('Polarization', ('TE', 'TM'))
pol2 = st.sidebar.radio('Polarization', ('TE', 'TM'))

st.sidebar.write('Refractive indices')
ns = st.sidebar.number_input('ns (x < -a)', 1.0, 5.0, 1.5, format='%0.6f')
n1 = st.sidebar.number_input('n1 (-a < x < a)', 1.0, 5.0, 1.55, format='%0.6f')
n0 = st.sidebar.number_input('n0 (x > a)', 1.0, 5.0, 1.5, format='%0.6f')
st.sidebar.write(t*2)


amp = st.sidebar.slider('Slider', 0.0, 2.0, 1.0, 0.1)
n = st.sidebar.slider('n', 0.0, 4.0, 1.0, 0.1)
x = np.linspace(0, 2*n*np.pi, 100)
y = amp * np.sin(x)
plt.subplot(121)
plt.ylim([-2,2])
plt.xlabel('x')
plt.ylabel('sin')
plt.plot(x, y)

plt.subplot(122)
plt.ylim([-2,2])
y2 = amp * np.cos(x)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('cos')

st.pyplot(plt)
s = 'Effective index = {0}'.format(1.54323)
st.write(s)