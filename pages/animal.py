import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Salud", page_icon="🩺")

st.title('Novus Mando - Salud 🩺')

st.header("Soluciones en la Nube para la Salud Animal 🦜")
st.title('Solución 1: Salvar a los animales de los ensayos 🏥clínicos💉 de 🧪toxicidad☣️')
st.markdown(
  """
  La primera solución para la Salud Animal incluye:
  - 📝 _    Diagnóstico de tipo de Test Alternativo ante requisitos de moléculas y KPIs
  - 📆 _    Alarmas de toxicidad por tipos de células
  - 📍 _    Recomendaciones para minimizar toxicidad
  
  EMPIEZA TU CENTRO DE 🩺SALUD ANIMAL🦜 AHORA 🕰
  """
)
