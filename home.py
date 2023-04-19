import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Salud", page_icon="🩺")

st.title('Novus Salud 🩺')
st.header("Soluciones en la Nube para toda la cadena de la Salud")
st.write("Bienvenidos al futuro que se nos hizo presente 👋")
st.markdown(
  """
  En esta web encontrarás los 3 sistemas iniciales de Inteligencia Artificial de Novus Salud:
  - 📝 _    Diagnóstico Personalizado del Paciente: atención y alarmas patológicas
  - 📆 _    Calendario Personalizado de Rehabilitación: Sistema de Recomendación de Intervención
  - 📍 _    Evaluación Personalizada de Evolución y Prevención
  
  EMPIEZA TU CENTRO DE SALUD AHORA 🕰
  """
)

st.title('1. Diagnóstico Personalizado 📝')


st.title('2. Calendario de Atención Personalizado 📅')


st.title('3. Evaluación y Monitoreo Personalizado en Tiempo Real 📍')
