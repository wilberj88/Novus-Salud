import streamlit as st
import time

st.title('Cronómetro de los suicidios en España')


ph = st.empty()
N = 180*60
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Minutos que faltan promedio para el próximo suicidio de un hombre en España", f"{mm:02d}:{ss:02d}")
    time.sleep(1)        

