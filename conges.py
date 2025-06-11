import streamlit as st
import pandas as pd

# Charger les données (déjà générées avec ton script)
df_resultats = pd.read_excel("resultats_cp.xlsx")

# Résumé par salarié
df_resume = df_resultats.groupby("Nom", as_index=False)[["CP N-1", "CP N"]].sum()

st.title("📋 Résumé des Congés Payés par Salarié")

# Affichage tableau résumé
st.subheader("🔹 Synthèse globale")
st.dataframe(df_resume, use_container_width=True)

# Affichage détails par salarié
st.subheader("🔎 Détails par salarié")
nom_selectionne = st.selectbox("Choisir un salarié :", df_resultats["Nom"].unique())

df_detail = df_resultats[df_resultats["Nom"] == nom_selectionne]
st.dataframe(df_detail[["Page", "Libellé", "CP N-1", "CP N"]].sort_values("Page"), use_container_width=True)
