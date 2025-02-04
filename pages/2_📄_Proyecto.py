import streamlit as st

st.title("📄 Detalles del Proyecto")

with st.expander("📌 Objetivos principales", expanded=True):
    st.markdown("""
    - Crear una plataforma innovadora para...
    - Implementar algoritmos de machine learning...
    - Proporcionar una experiencia de usuario excepcional
    """)

st.header("🚀 Tecnologías utilizadas")
cols = st.columns(3)
with cols[0]:
    st.markdown("### Frontend")
    st.code("""
    - Streamlit
    - React
    - Tailwind CSS
    """)

with cols[1]:
    st.markdown("### Backend")
    st.code("""
    - Python
    - FastAPI
    - PostgreSQL
    """)

with cols[2]:
    st.markdown("### IA/ML")
    st.code("""
    - TensorFlow
    - PyTorch
    - OpenAI API
    """)

st.header("📅 Cronograma")
st.timeline([
    {"title": "Fase 1: Diseño", "date": "2024-01"},
    {"title": "Fase 2: Desarrollo", "date": "2024-04"},
    {"title": "Fase 3: Lanzamiento", "date": "2024-09"}
])
