import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
st.set_page_config(page_title="Dashboard", layout='wide',
                   initial_sidebar_state='auto')
def procesar_archivo_excel(archivo):
    dfs=[]
    for sheet_name in archivo.sheet_names:
        df = pd.read_excel(archivo, sheet_name=sheet_name)
        columnas_interes = ["Fecha", "CO (ug/m3)", "H2S (ug/m3)", "NO2 (ug/m3)", "O3 (ug/m3)",
                            "PM10 (ug/m3)", "PM2.5 (ug/m3)", "SO2 (ug/m3)", "Ruido (dB)",
                            "UV", "Humedad (%)", "Presion (Pa)", "Temperatura (C)"]
        df = df[columnas_interes]
        df = df.replace('-', np.nan)
        df = df.fillna(0)
        dfs.append(df)
    return dfs
def main():
    anio = st.sidebar.radio("Seleccione el año", options=[2020, 2021])
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
         'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes_seleccionado = st.sidebar.selectbox("Seleccione el mes", options=meses)
    archivos = []
    ubicaciones = []
    if anio == 2020:
        if mes_seleccionado.lower() == "julio":
            archivo = pd.ExcelFile("Monitoreo_julio.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "agosto":
            archivo = pd.ExcelFile("Monitoreo_agosto.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "setiembre":
            archivo1 = pd.ExcelFile("Monitoreo_setiembre_Bonilla.xlsx")
            archivo2 = pd.ExcelFile("Monitoreo_setiembre_Ov.Miraflores.xlsx")
            archivos.append(archivo1)
            archivos.append(archivo2)
            ubicaciones.append(
                "Complejo Deportivo Manuel Bonilla")
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "octubre":
            archivo = pd.ExcelFile("Monitoreo_octubre.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "noviembre":
            archivo = pd.ExcelFile("6_Monitoreo_Noviembre.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "diciembre":
            archivo = pd.ExcelFile("7_Monitoreo_Diciembre.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
    elif anio == 2021:
        if mes_seleccionado.lower() == "enero":
            archivo = pd.ExcelFile("8_Monitoreo_Enero_2021.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "febrero":
            archivo = pd.ExcelFile("9_Monitoreo_Febrero_2021.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "marzo":
            archivo = pd.ExcelFile("10_Monitoreo_Marzo_2021.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "abril":
            archivo = pd.ExcelFile("11_Monitoreo_Abril_2021.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "mayo":
            archivo = pd.ExcelFile("12_Monitoreo_Mayo_2021.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")
        elif mes_seleccionado.lower() == "junio":
            archivo = pd.ExcelFile("13_Monitoreo_Junio_2021.xlsx")
            archivos.append(archivo)
            ubicaciones.append("Óvalo de Miraflores")

    if archivos:
        st.subheader(
            f"Mediciones de Calidad de Aire - {mes_seleccionado.capitalize()} {anio}")
        for archivo, ubicacion in zip(archivos, ubicaciones):
            dfs = procesar_archivo_excel(archivo)
            if dfs:
                for i, df in enumerate(dfs):
                    if len(archivo.sheet_names) > 1:
                        if i == 0:
                            st.markdown(
                                "📍 Complejo Deportivo Manuel Bonilla")
                        else:
                            st.markdown(
                                "📍 Óvalo de Miraflores")
                    else:
                        st.markdown(f"📍 {ubicacion}")

                    for columna in df.columns[1:]:
                        st.subheader(columna)
                        fig = px.line(df, x="Fecha", y=columna)
                        st.plotly_chart(fig)
                    st.snow()
            else:
                st.warning(
                    "Los archivos seleccionados no contienen datos válidos.")
    else:
        st.warning("No se encontró archivo para el año y mes seleccionado.")

if __name__ == "__main__":
    main()
