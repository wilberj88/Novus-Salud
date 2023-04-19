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
st.header("Soluciones en la Nube para la Salud Mental 🧠")

st.title('Datos del Suicidio en España 2021 📝')
data = {'Año': [2021, 2020],
        'Suicidios Totales': [4003, 3941],
        'Suicidios Masculinos': [2982, 2933],
        'Suicidios Femeninos': [1021, 1008],
        'Suicidios Infanto-Juveniles': [22, 11],
        'Suicidios Adultos>70': [999, 980]}

df = pd.DataFrame(data)
st.dataframe(df)
st.write('Fuente: Observatorio del Suicidio en España (https://www.fsme.es/observatorio-del-suicidio-2021/)')


st.title('Desafío Diario del Suicidio en España')
col1, col2, col3, col4 = st.columns(4)
col1.metric("Hombres", "8", "1,8%")
col2.metric("Mujeres", "2,8", "1%")
col3.metric("Mayores de 70", "2,7", "2%")
col4.metric("Niños", "0,06", "50%")
st.write('Crecimiento Interanual 2021 Vs 2020 en verde. Cálculos Novus Salud. Fuente: Observatorio del Suicidio en España')


st.title('Oportunidad de Predicción Oportuna')
col5, col6 = st.columns(2)
col5.metric("Intentos x Suicidio", "20", "NA")
col6.metric("Intentos anuales en España", "80000", "NA")
st.write('Tenemos 19 intentos para detectar interés de suicidio')
st.write('Podemos rastrear los intentos previos o potenciales mediante diagnósticos')


st.write("""
**Propuesta de Solución desde Novus Salud 🩺**
- Análisis de Sentimiento en Tiempo Real que `Predice Riesgo de Suicidio` con `ChatGPT & Whisper` engines
""")
st.write('---')

st.title('1. Diagnóstico Personalizado 📝')
st.write('Video Preguntas Aleatorias')
st.write('Análisis de Sentimiento en Texto y Video')
st.write('Resultados Vs Promedio Nacional')
def render_basic_radar():
    option = {
        "title": {"text": "Previo Votación 🗳️"},
        "legend": {"data": ["Candidato A", "Candidato B"]},
        "radar": {
            "indicator": [
                {"name": "Líderes", "max": 6500},
                {"name": "Financiación", "max": 16000},
                {"name": "Sentimiento", "max": 30000},
                {"name": "Votación Anterior", "max": 38000},
                {"name": "Interaciones", "max": 52000},
                {"name": "Recordación de Marca", "max": 25000},
            ]
        },
        "series": [
            {
                "name": "Aprendizaje Actual Vs Proyectado",
                "type": "radar",
                "data": [
                    {
                        "value": [2000, 10000, 20000, 3500, 15000, 11800],
                        "name": "Candidato A",
                    },
                    {
                        "value": [3500, 15000, 25000, 10800, 22000, 20000],
                        "name": "Candidato B",
                    },
                ],
            }
        ],
    }
    st_echarts(option, height="500px")
ST_RADAR_DEMOS = {
    "Radar: Basic Radar": (
        render_basic_radar,
        "https://echarts.apache.org/examples/en/editor.html?c=radar",
    ),
}
render_basic_radar()


st.title('2. Calendario de Atención Personalizado 📅')


st.title('3. Evaluación y Monitoreo Personalizado en Tiempo Real 📍')
