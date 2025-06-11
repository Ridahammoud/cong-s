import streamlit as st
import pandas as pd

st.title("📋 Résumé des Congés Payés par Salarié")

# 📂 Upload du fichier Excel
fichier_excel = st.file_uploader("Chargez le fichier Excel généré par le script", type=["xlsx"])

if fichier_excel:
    df_resultats = pd.read_excel(fichier_excel)

    # Résumé par salarié
    df_resume = df_resultats.groupby("Nom", as_index=False)[["CP N-1", "CP N"]].sum()

    st.subheader("🔹 Synthèse globale")
    st.dataframe(df_resume, use_container_width=True)

    st.subheader("🔎 Détails par salarié")
    nom_selectionne = st.selectbox("Choisir un salarié :", df_resultats["Nom"].unique())
    df_detail = df_resultats[df_resultats["Nom"] == nom_selectionne]
    st.dataframe(df_detail[["Page", "Libellé", "CP N-1", "CP N"]].sort_values("Page"), use_container_width=True)

else:
    st.warning("Veuillez d'abord téléverser un fichier Excel contenant les résultats.")
