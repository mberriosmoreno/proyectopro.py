import streamlit as st
from PIL import Image

# Configuración inicial
st.set_page_config(
    page_title="Mi Proyecto Innovador",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar estilo personalizado
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar con logo y navegación
with st.sidebar:
    logo = Image.open("assets/images/logo.png")
    st.image(logo, width=200)
    
    st.title("Navegación")
    st.page_link("app.py", label="Inicio", icon="🏠")
    st.page_link("pages/1_🏠_Inicio.py", label="Introducción", icon="🌍")
    st.page_link("pages/2_📄_Proyecto.py", label="Detalles del Proyecto", icon="📊")
    
    st.divider()
    st.success("**Estado del proyecto:** En desarrollo activo")
    st.info("**Versión:** 1.0.0 | **Última actualización:** Julio 2024")

# Contenido principal de la página de inicio
st.title("🌟 Bienvenido a Mi Proyecto Innovador")
st.subheader("Revolucionando la forma de interactuar con la tecnología")

with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Características principales
        - ✅ Interfaz moderna e intuitiva
        - 📈 Analíticas en tiempo real
        - 🤖 Integración con IA
        - 🔒 Seguridad de primer nivel
        """)
    with col2:
        st.image("assets/images/demo.gif", caption="Demo interactiva")

st.divider()
