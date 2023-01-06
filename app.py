import streamlit as st
import numpy as np
import time

st.set_page_config(
    page_title="Digital Comm Calculator",
    page_icon="ect.ico",
    layout="wide",
    menu_items={
        'About': "App contentsL Copyright Julio Aráuz, 2023"
    }
)

resultComputeOne = 1

def computeOne(a):
  resultComputeOne = a*2

st.image("ohio_logo_small.svg", width=200)
# SVG needed to be optimized svg from Inkscape save as to work
st.caption("McClure School of Emerging Communicaton Technologies")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Power", "Path loss", "Free space propagation", "SNR", "Shannon"])

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
    output = "{:.4e}".format(pmW)
    st.write('Power in [mW] is = ', output, 'mW')
    st.latex(r'''P_{mW}=10^{\left( \frac{P_{dBm}}{10} \right )}''')      


with tab2:
  col1, col2 = st.columns(2)
  with col1:
    st.subheader('Free space path loss')
    st.caption('Type values of known parameters in the boxes.')
    n3 = st.number_input('Distance Tx to Rx in [Km]', key='n3')
    n4 = st.number_input('Frequency in [MHz]', key='n4')
    n5 = st.number_input('Path loss in [dB]', key='n4')
    st.latex(r'''PL_{dB}=20 \times log_{10}(d_{Km})+20 \times log_{10}(f_{MHz})+32.45''')      


  result1 = st.button(label="Compute path loss PL in [dB]")
  result2 = st.button(label="Compute distance d in [Km]")
  result3 = st.button(label="Compute frequency f in [MHz]")
  

  with col2:
    st.subheader('Model results')
    st.caption('Use the buttons to compute the unknown parameter and display the results.')
    if result1:
        pl = (20*np.log10(n3))+(20*np.log10(n4))+32.45
        output = "{:.4f}".format(pl)
        st.write('Distance Tx to Rx in [Km] is ', n3, 'Km')
        st.write('Frequency in [MHz] is ', n4, 'MHz')
        st.write('Path loss in [dB] is ', output, 'dB')
    if result2:
        d = np.power(10,((n5 - 32.45 - (20*np.log10(n4)))/20))
        output = "{:.4f}".format(d)
        st.write('Frequency in [MHz] is ', n4, 'MHz')
        st.write('Path loss in [dB] is ', n5, 'dB')
        st.write('Distance Tx to Rx in [Km] is ', output, 'Km')
        st.latex(r'''d_{Km} = 10^{\frac{PL_{dB} - 32.45 - 20 \times log_{10}(f_{MHz})}{20}}''')      
    if result3:
        f = np.power(10,((n5 - 32.45 - (20*np.log10(n3)))/20))
        output = "{:.4f}".format(f)
        st.write('Path loss in [dB] is ', n5, 'dB')
        st.write('Distance Tx to Rx in [Km] is ', n3, 'Km')
        st.write('Frequency in [MHz] is ', output, 'MHz')
        st.latex(r'''f_{MHz} = 10^{\frac{PL_{dB} - 32.45 - 20 \times log_{10}(d_{Km})}{20}}''')    

  
with tab3:
  col1, col2 = st.columns(2)
  with col1:
    st.subheader('Free space propagation')
    st.caption('Type values of known parameters in the boxes.')
    n6 = st.number_input('Power received in [dBm] (Prx)', key='n6')
    n7 = st.number_input('Power transmitted in [dBm] (Ptx)', key='n7')
    n8 = st.number_input('Path Loss in [dB] (PL)', key='n8')
    n9 = st.number_input('Gain transmitting antenna [dB] (Gtx)', key='n9')
    n10 = st.number_input('Gain receiving antenna [dB] (Grx)', key='n10')
    st.latex(r'''Prx_{[dBm]}=Ptx_{[dBm]}-PL_{[dB]}+Gtx_{[dB]}+Grx_{[dB]}''')

    result4 = st.button(label="Compute Prx in [dBm]")
    result5 = st.button(label="Compute Ptx in [dBm]")
    result6 = st.button(label="Compute PL in [dB]")
    result7 = st.button(label="Compute Gtx in [dB]")
    result8 = st.button(label="Compute Grx in [dB]")
    
  with col2:
    st.subheader('Model results')
    st.caption('Use the buttons to compute the unknown parameter and display the results.')
    if result4:
      prx = n7-n8+n9+n10
      output = "{:.4f}".format(prx)
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Power received in [dBm] is ', output, '[dBm]')

    if result5:
      ptx = n6+n8-n9-n10
      output = "{:.4f}".format(ptx)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Power transmitted in [dBm] is ', output, '[dBm]')
      st.latex(r'''Ptx_{[dBm]}=Prx_{[dBm]}+PL_{[dB]}-Gtx_{[dB]}-Grx_{[dB]}''')

    if result6:
      pl = n7-n6+n9+n10
      output = "{:.4f}".format(pl)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Path loss in [dB] is ', output, '[dB]')
      st.latex(r'''PL_{[dB]}=Ptx_{[dBm]}-Prx_{[dBm]}+Gtx_{[dB]}+Grx_{[dB]}''')

    if result7:
      gtx = n6-n7+n8-n10
      output = "{:.4f}".format(gtx)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', output, '[dB]')
      st.latex(r'''Gtx_{[dB]}=Ptx_{[dBm]}-Prx_{[dBm]}+PL_{[dB]}-Grx_{[dB]}''')

    if result8:
      grx = n6-n7+n8-n9
      output = "{:.4f}".format(grx)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', output, '[dB]')
      st.latex(r'''Grx_{[dB]}=Ptx_{[dBm]}-Prx_{[dBm]}+PL_{[dB]}-Gtx_{[dB]}''')

with tab4:
  st.subheader("Signal to noise ratio (SNR) computations")
  col1, col2, col3 = st.columns(3, gap="large")
  with col1:
    st.caption('Enter signal and noise powers in mW to compute SNR in numerical format and dB.')
    n11 = st.number_input('Signal power in [mW] (Ps)', key='n11', format='%.10f')
    n12 = st.number_input('Noise power in [mW] (Pn)', key='n12', format='%.4e')
    st.write('Signal power in [mW] = ', n11)
    st.write('Noise power in [mW] = ', n12)
    snr_nf = np.divide(n11,n12)
    snr_db = 10 * np.log10(np.divide(n11,n12))
    output1 = "{:.4f}".format(snr_nf)
    output2 = "{:.4f}".format(snr_db)
    if n12==0:
      output1 = np.inf
      output2 = np.inf
    st.write('SNR (numerical) is ', output1)
    st.write('SNR in [dB] is', output2, 'dB')
    st.latex(r'''\text{SNR}=\frac{P_s}{P_n}''')
    st.latex(r'''\text{SNR}_{dB}=10 \times log_{10} \left( \frac{P_s}{P_n} \right )''')

  with col2:
    st.caption('Enter signal and noise powers in dBm to compute SNR in numerical format and dB.')
    n13 = st.number_input('Signal power in [dBm] (Ps)', key='n13', format='%.4f')
    n14 = st.number_input('Noise power in [dBm] (Pn)', key='n14', format='%.4e')
    st.write('Signal power in [dBm] = ', n13)
    st.write('Noise power in [dBm] = ', n14)
    snr_db = n13 - n14
    snr_nf = np.power(10,np.divide(snr_db,10))
    output1 = "{:.4f}".format(snr_nf)
    output2 = "{:.4f}".format(snr_db)
    st.write('SNR (numerical) is ', output1)
    st.write('SNR in [dB] is', output2, 'dB')
    st.latex(r'''\text{SNR}_{dB}=P_s [\text{dBm}] - P_n [\text{dBm}]''')

  with col3:
    st.caption('Enter SNR in numerical format or in dB. Compute SNR in both formats.')
    n15 = st.number_input('SNR numerical format (SNR)', key='n15', format='%.4f')
    n16 = st.number_input('SNR in [dB] (SNR)', key='n16', format='%.4f')
    result9 = st.button(label="Compute SNR in dB")
    result10 = st.button(label="Compute numerical SNR")

    if result9:
      snr_db = 10 * np.log10(n15)
      output1 = "{:.4f}".format(snr_db)
      st.write('For SNR ', n15, '(numerical format) ', ', SNR in [dB] is', output1, 'dB')
      st.latex(r'''\text{SNR}_{dB}=10 \times log_{10} (\text{SNR})''')
    if result10:
      snr_nf = np.power(10,n16/10)
      output2 = "{:.4f}".format(snr_nf)
      st.write('For SNR ', n16, '[dB] ', ', SNR (numerical) is ', output2)
      st.latex(r'''\text{SNR}=10^{\left ( \frac{\text{SNR}_{dB}}{10} \right )} ''')

with tab5:
  st.subheader("Shannon-Hartley channel bandwidth")

