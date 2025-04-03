# streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Antraco – Preditivo Farmacotécnico")

st.title("🧪 Antraco – Plataforma Preditiva Farmacotécnica")
st.subheader("Simulação baseada em dados de excipientes e API")

# Fórmula simulada
data = {
    'Componente': ['Ibuprofeno', 'Microcelac 100', 'Crospovidona', 'Estearilfumarato de Sódio', 'Aerosil R972', 'Eudragit E PO'],
    'Quantidade (%)': [46.5, 40.0, 5.0, 1.0, 0.6, 6.9],
    'Higroscopicidade': [0.2, 0.35, 0.4, 0.05, 0.01, 0.15],
    'Compressibilidade': [0.2, 0.85, 0.6, 0.1, 0.05, 0.3],
    'Risco de Incompatibilidade': [0.4, 0.3, 0.2, 0.5, 0.1, 0.2]
}
df = pd.DataFrame(data)
df['Fração'] = df['Quantidade (%)'] / 100

st.write("### Fórmula base (simulada):")
st.dataframe(df)

# Cálculos preditivos
H_formula = (df['Higroscopicidade'] * df['Fração']).sum()
C_formula = (df['Compressibilidade'] * df['Fração']).sum()
R_formula = (df['Risco de Incompatibilidade'] * df['Fração']).sum()

st.write("### Parâmetros preditivos estimados:")
st.metric("H_formula (Higroscopicidade)", round(H_formula, 3))
st.metric("C_formula (Compressibilidade)", round(C_formula, 3))
st.metric("R_formula (Risco de Incompatibilidade)", round(R_formula, 3))

# Curva predita de dissolução
st.write("### Curva predita de dissolução")
tempo = [0, 5, 10, 15, 30, 45, 60, 90]
liberacao = [0, 10, 20, 45, 80, 95, 98, 99]
fig = px.line(x=tempo, y=liberacao, labels={'x': 'Tempo (min)', 'y': 'Liberação (%)'})
st.plotly_chart(fig)
