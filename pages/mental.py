import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import time



# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Salud", page_icon="🩺")

st.title('Novus Mando - Salud 🩺')
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

st.title('Cronómetro de los suicidios en España')
ph = st.empty()
N = 5*60
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    time.sleep(1)
st.write(crono_hombres)



st.write("""
**Propuesta de Solución desde Novus Salud 🩺**
- Análisis de Sentimiento en Tiempo Real que `Predice Riesgo de Suicidio` con `ChatGPT & Whisper` engines
""")
st.write('---')

st.title('1. Diagnóstico Personalizado 📝')
st.write('')

st.text_input('Ingresa la URL de la red social en versión pública a analizar:')

st.write('Video Preguntas Aleatorias')
picture = st.camera_input("Responde en 30 segundos la siguiente pregunta: ¿Bla Bla bla?")
if picture:
    st.image(picture)
    st.write('Cargar Respuesta 🤖')

st.write('Análisis de Sentimiento en Texto y Video')
col7, col8 = st.columns(2)
col7.metric("Riesgo en Voz", "68%", "15%")
col8.metric("Riesgo en Video", "57%", "10%")
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
def render_heatmap_cartesian():
    hours = [
        "12a",
        "1a",
        "2a",
        "3a",
        "4a",
        "5a",
        "6a",
        "7a",
        "8a",
        "9a",
        "10a",
        "11a",
        "12p",
        "1p",
        "2p",
        "3p",
        "4p",
        "5p",
        "6p",
        "7p",
        "8p",
        "9p",
        "10p",
        "11p",
    ]
    days = [
        "Saturday",
        "Friday",
        "Thursday",
        "Wednesday",
        "Tuesday",
        "Monday",
        "Sunday",
    ]

    data = [
        [0, 0, 5],
        [0, 1, 1],
        [0, 2, 0],
        [0, 3, 0],
        [0, 4, 0],
        [0, 5, 0],
        [0, 6, 0],
        [0, 7, 0],
        [0, 8, 0],
        [0, 9, 0],
        [0, 10, 0],
        [0, 11, 2],
        [0, 12, 4],
        [0, 13, 1],
        [0, 14, 1],
        [0, 15, 3],
        [0, 16, 4],
        [0, 17, 6],
        [0, 18, 4],
        [0, 19, 4],
        [0, 20, 3],
        [0, 21, 3],
        [0, 22, 2],
        [0, 23, 5],
        [1, 0, 7],
        [1, 1, 0],
        [1, 2, 0],
        [1, 3, 0],
        [1, 4, 0],
        [1, 5, 0],
        [1, 6, 0],
        [1, 7, 0],
        [1, 8, 0],
        [1, 9, 0],
        [1, 10, 5],
        [1, 11, 2],
        [1, 12, 2],
        [1, 13, 6],
        [1, 14, 9],
        [1, 15, 11],
        [1, 16, 6],
        [1, 17, 7],
        [1, 18, 8],
        [1, 19, 12],
        [1, 20, 5],
        [1, 21, 5],
        [1, 22, 7],
        [1, 23, 2],
        [2, 0, 1],
        [2, 1, 1],
        [2, 2, 0],
        [2, 3, 0],
        [2, 4, 0],
        [2, 5, 0],
        [2, 6, 0],
        [2, 7, 0],
        [2, 8, 0],
        [2, 9, 0],
        [2, 10, 3],
        [2, 11, 2],
        [2, 12, 1],
        [2, 13, 9],
        [2, 14, 8],
        [2, 15, 10],
        [2, 16, 6],
        [2, 17, 5],
        [2, 18, 5],
        [2, 19, 5],
        [2, 20, 7],
        [2, 21, 4],
        [2, 22, 2],
        [2, 23, 4],
        [3, 0, 7],
        [3, 1, 3],
        [3, 2, 0],
        [3, 3, 0],
        [3, 4, 0],
        [3, 5, 0],
        [3, 6, 0],
        [3, 7, 0],
        [3, 8, 1],
        [3, 9, 0],
        [3, 10, 5],
        [3, 11, 4],
        [3, 12, 7],
        [3, 13, 14],
        [3, 14, 13],
        [3, 15, 12],
        [3, 16, 9],
        [3, 17, 5],
        [3, 18, 5],
        [3, 19, 10],
        [3, 20, 6],
        [3, 21, 4],
        [3, 22, 4],
        [3, 23, 1],
        [4, 0, 1],
        [4, 1, 3],
        [4, 2, 0],
        [4, 3, 0],
        [4, 4, 0],
        [4, 5, 1],
        [4, 6, 0],
        [4, 7, 0],
        [4, 8, 0],
        [4, 9, 2],
        [4, 10, 4],
        [4, 11, 4],
        [4, 12, 2],
        [4, 13, 4],
        [4, 14, 4],
        [4, 15, 14],
        [4, 16, 12],
        [4, 17, 1],
        [4, 18, 8],
        [4, 19, 5],
        [4, 20, 3],
        [4, 21, 7],
        [4, 22, 3],
        [4, 23, 0],
        [5, 0, 2],
        [5, 1, 1],
        [5, 2, 0],
        [5, 3, 3],
        [5, 4, 0],
        [5, 5, 0],
        [5, 6, 0],
        [5, 7, 0],
        [5, 8, 2],
        [5, 9, 0],
        [5, 10, 4],
        [5, 11, 1],
        [5, 12, 5],
        [5, 13, 10],
        [5, 14, 5],
        [5, 15, 7],
        [5, 16, 11],
        [5, 17, 6],
        [5, 18, 0],
        [5, 19, 5],
        [5, 20, 3],
        [5, 21, 4],
        [5, 22, 2],
        [5, 23, 0],
        [6, 0, 1],
        [6, 1, 0],
        [6, 2, 0],
        [6, 3, 0],
        [6, 4, 0],
        [6, 5, 0],
        [6, 6, 0],
        [6, 7, 0],
        [6, 8, 0],
        [6, 9, 0],
        [6, 10, 1],
        [6, 11, 0],
        [6, 12, 2],
        [6, 13, 1],
        [6, 14, 3],
        [6, 15, 4],
        [6, 16, 0],
        [6, 17, 0],
        [6, 18, 0],
        [6, 19, 0],
        [6, 20, 1],
        [6, 21, 2],
        [6, 22, 2],
        [6, 23, 6],
    ]
    data = [[d[1], d[0], d[2] if d[2] != 0 else "-"] for d in data]

    option = {
        "tooltip": {"position": "top"},
        "grid": {"height": "50%", "top": "10%"},
        "xAxis": {"type": "category", "data": hours, "splitArea": {"show": True}},
        "yAxis": {"type": "category", "data": days, "splitArea": {"show": True}},
        "visualMap": {
            "min": 0,
            "max": 10,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "15%",
        },
        "series": [
            {
                "name": "Punch Card",
                "type": "heatmap",
                "data": data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
            }
        ],
    }
    st_echarts(option, height="500px")


ST_HEATMAP_DEMOS = {
    "Heatmap: Heatmap Cartesian": (
        render_heatmap_cartesian,
        "https://echarts.apache.org/examples/en/editor.html?c=heatmap-cartesian",
    ),
}

render_heatmap_cartesian()

st.title('3. Evaluación y Monitoreo Personalizado en Tiempo Real 📍')
col8, col9, col10 = st.columns(3)
with col8:
  acelerometro1 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 25, "name": "Concejales"}],
            }
        ],
    }

  st_echarts(options=acelerometro1)

with col9:
  acelerometro2 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 90, "name": "Votos"}],
            }
        ],
    }

  st_echarts(options=acelerometro2)

with col10:
  acelerometro3 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 66, "name": "Sentimiento"}],
            }
        ],
    }
  st_echarts(options=acelerometro3)
