import streamlit as st
import numpy as np
import time

resultComputeOne = 1

def computeOne(a):
  resultComputeOne = a*2

st.image("ohio_logo_small.svg", width=200)
# SVG needed to be optimized svg from Inkscape save as to work
st.caption("McClure School of Emerging Communicaton Technologies")


tab1, tab2, tab3, tab4 = st.tabs(["Power", "Free space", "Owl", "Fox"])

with tab1:
  col1, col2 = st.columns(2)

  with col1:
    st.subheader('mW to dBm')
    n1 = st.number_input('Input power in [mW]', key='n1', format='%.4e')
    st.write('Power in [mW] = ', n1)
    # keys have to be different, but not necessarily match the
    # name of the returned variable e.g. n1 and n1
    pdBm = 10*np.log10(n1)
    output = "{:.4f}".format(pdBm)
    st.write('Power in [dBm] is = ', output, 'dBm')
    st.latex(r'''P_{dBm}=10 \times log_{10} \left( \frac{P_{mW}}{1mW}\right )''')

  with col2:
    st.subheader('dBm to mW')
    n2 = st.number_input('Input power in [dBm]', key='n2')
    st.write('Power in [dBm] = ', n2)
    pmW = np.power(10,n2/10)
    output = "{:.4f}".format(pmW)
    st.write('Power in [mW] is = ', output, 'mW')
    st.latex(r'''P_{mW}=10^{\left( \frac{P_{dBm}}{10} \right )}''')      


with tab2:
  col1, col2 = st.columns(2)
  with col1:
    st.subheader('Free space propagation')
    n3 = st.number_input('Input a', key='n3')
    n4 = st.number_input('Input b', key='n4')

  result1 = st.button(label="times2")
  result2 = st.button(label="times3")

  with col2:
    st.subheader('Model results')
    if result1:
        st.write('res1:', str(n3*2))
    if result2:
        st.write('res2:', str(n3*3))
        

  
with tab3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg", width=290)

with tab4:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg", width=290)
