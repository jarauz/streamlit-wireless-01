import streamlit as st
import numpy as np
import time




tab1, tab2, tab3 = st.tabs(["Input Fields", "Sliders", "Owl"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        n1 = st.number_input('Insert a number', key='n1')
        st.write('The first number is ', n1)
        # keys have to be different, but not necessarily match the
        # name of the returned variable e.g. n1 and n1


    with col2:
        n2 = st.number_input('Insert a number', key='n2')
        st.write('The second number is ', n2)
      
    st.write('The sum of the two numbers is: ', n1 + n2)

with tab2:
    values1 = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0), key='values1')
    st.write('Values:', values1)
  
    values2 = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0), key='values2')
    st.write('Values:', values2)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
