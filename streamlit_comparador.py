import streamlit as st
import json
import os
from glob import glob

st.title("📚 Comparação de Respostas de LLMs - Análise de Texto em Latim")

# Listar arquivos JSON gerados
json_files = sorted(glob("output/respostas_latim_*.json"), reverse=True)

if not json_files:
    st.warning("Nenhum arquivo de resposta foi encontrado.")
    st.stop()

selected_file = st.selectbox("Escolha um arquivo para visualizar:", json_files)

with open(selected_file, "r", encoding="utf-8") as f:
    data = json.load(f)

st.subheader("📋 Texto analisado:")
st.markdown(f"`Quo usque tandem abutere, Catilina, patientia nostra?`")

st.subheader("🧠 Respostas por LLM")

for model, resposta in data.items():
    st.markdown(f"### 🤖 {model.upper()}")
    st.markdown(resposta)
    st.markdown("---")
