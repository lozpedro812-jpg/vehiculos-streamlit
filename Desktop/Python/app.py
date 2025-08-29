import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análisis de Vehículos en EE.UU.",
    page_icon="🚗",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

car_data = load_data()

st.title("🚘 Análisis de Anuncios de Vehículos en EE.UU.")
st.markdown("Explora los datos de vehículos usados publicados en EE.UU. con filtros interactivos y visualizaciones dinámicas.")

st.sidebar.header("🔍 Filtros")
car_type = st.sidebar.selectbox("Tipo de coche", car_data["type"].dropna().unique())
year_range = st.sidebar.slider(
    "Año del modelo",
    int(car_data["model_year"].min()),
    int(car_data["model_year"].max()),
    (2010, 2020)
)
price_range = st.sidebar.slider(
    "Rango de precio",
    int(car_data["price"].min()),
    int(car_data["price"].max()),
    (2000, 20000)
)

filtered_data = car_data[
    (car_data["type"] == car_type) &
    (car_data["model_year"].between(year_range[0], year_range[1])) &
    (car_data["price"].between(price_range[0], price_range[1]))
]

st.subheader("📊 Visualizaciones Interactivas")

col1, col2 = st.columns(2)

with col1:
    if st.button("Construir histograma", key="btn_hist"):
        st.markdown("#### Histograma de odómetro")
        fig = px.histogram(filtered_data, x="odometer", nbins=30, title="Distribución del odómetro")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    if st.button("Construir gráfico de dispersión", key="btn_scatter"):
        st.markdown("#### Dispersión entre odómetro y precio")
        fig = px.scatter(filtered_data, x="odometer", y="price", color="condition", title="Odómetro vs Precio")
        st.plotly_chart(fig, use_container_width=True)

with st.expander("📋 Ver datos filtrados"):
    st.dataframe(filtered_data)





