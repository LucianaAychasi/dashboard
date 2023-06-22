import pandas as pd
import streamlit as st
import plotly.express as px
url = "https://www.datosabiertos.gob.pe/sites/default/files/13_Monitoreo_Junio_2021.xlsx"
df = pd.read_excel(url)
# Convertir la columna 'Fecha' al formato de fecha y hora
# df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y %H:%M', errors='coerce')
# Soltar filas con valores 'Fecha' faltantes
# df = df.dropna(subset=['Fecha'])
# Convertir 'Humedad (%)' columnna a numerico
# df['Humedad (%)'] = pd.to_numeric(df['Humedad (%)'], errors='coerce')
# Establecer 'Fecha' como índice
# df.set_index('Fecha', inplace=True)
# Vuelva a muestrear los datos a la frecuencia por hora
# df_hourly = df.resample('H').mean()
st.set_page_config(page_title="Dashboard", layout='centered', initial_sidebar_state='collapsed')

st.markdown('### Humedad ambiente')
fig = px.line(df, x="Fecha", y="Humedad (%)", title='Humedad (%)', markers=True, text='Humedad (%)')
fig.update_traces(line_color='#98EECC')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Temperatura ambiente')
fig = px.line(df, x="Fecha", y="Temperatura (C)", title='Temperatura (C)', markers=True, text='Temperatura (C)')
fig.update_traces(line_color='#FFC93C')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Monoxido de carbono')
fig = px.line(df, x="Fecha", y="CO (ug/m3)", title='Monoxido de carbono', markers=True, text='CO (ug/m3)')
fig.update_traces(line_color='#9DB2BF')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Ácido sulfhídrico')
fig = px.line(df, x="Fecha", y="H2S (ug/m3)", title='Ácido sulfhídrico', markers=True, text='H2S (ug/m3)')
fig.update_traces(line_color='#EEE2DE')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Dióxido de nitrógeno')
fig = px.line(df, x="Fecha", y="NO2 (ug/m3)", title='Dióxido de nitrógeno', markers=True, text='NO2 (ug/m3)')
fig.update_traces(line_color='#00ABB3')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Ozono')
fig = px.line(df, x="Fecha", y="O3 (ug/m3)", title='Ozono', markers=True, text='O3 (ug/m3)')
fig.update_traces(line_color='#39A2DB')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Partículas de menos de 10 micrómetros')
fig = px.line(df, x="Fecha", y="PM10 \n(ug/m3)", title='PM10', markers=True, text='PM10 \n(ug/m3)')
fig.update_traces(line_color='#A7BBC7')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Materia particulada 2.5')
fig = px.line(df, x="Fecha", y="PM2.5 \n(ug/m3)", title='PM2.5', markers=True, text='PM2.5 \n(ug/m3)')
fig.update_traces(line_color='#BDD2B6')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Dióxido de azufre')
fig = px.line(df, x="Fecha", y="SO2 (ug/m3)", title='Dióxido de azufre', markers=True, text='SO2 (ug/m3)')
fig.update_traces(line_color='#BDD2B6')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Ruido ambiente')
fig = px.line(df, x="Fecha", y="Ruido (dB)", title='Ruido', markers=True, text='Ruido (dB)')
fig.update_traces(line_color='#B799FF')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Rayos ultravioleta')
fig = px.line(df, x="Fecha", y="UV", title='Rayos ultravioleta', markers=True, text='UV')
fig.update_traces(line_color='#FF6969')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Presión atmosférica')
fig = px.line(df, x="Fecha", y="Presion \n(Pa)", title='Presión atmosférica', markers=True, text='Presion \n(Pa)')
fig.update_traces(line_color='#A555EC')
st.plotly_chart(fig, use_container_width=True)