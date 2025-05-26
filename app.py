import streamlit as st
import math

st.title("Calculadora Solar com Coordenadas")
st.write("Insira as coordenadas do local para estimar a angulação ideal e o número máximo de placas solares.")

lat = st.number_input("Latitude", value=-19.9, format="%.6f")
lon = st.number_input("Longitude", value=-43.9, format="%.6f")
area_disponivel = st.number_input("Área disponível para instalação (em m²)", value=30.0)

tamanho_placa_m2 = 1.7  # metros quadrados
potencia_placa_w = 450  # watts por placa

def angulo_ideal(latitude):
    return abs(latitude)

def placas_possiveis(area_total, area_placa):
    return math.floor(area_total / area_placa)

if st.button("Calcular"):
    angulo = angulo_ideal(lat)
    num_placas = placas_possiveis(area_disponivel, tamanho_placa_m2)
    potencia_total_kw = (num_placas * potencia_placa_w) / 1000

    st.success(f"Angulação ideal das placas: **{angulo:.1f}°**")
    st.success(f"Número máximo de placas: **{num_placas}**")
    st.success(f"Potência total estimada: **{potencia_total_kw:.2f} kW**")

    st.map(data={'lat': [lat], 'lon': [lon]}, zoom=16)
