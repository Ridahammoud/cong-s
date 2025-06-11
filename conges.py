import streamlit as st
import pandas as pd

st.title("📋 Résumé des Congés Payés par Salarié")

# 📁 Uploader
fichier_excel = st.file_uploader("🔽 Importer le fichier Excel des résultats de congés", type=["xlsx"])

if fichier_excel:
    try:
        # Charger le fichier Excel
        df_resultats = pd.read_excel(fichier_excel)

        # Créer un résumé par salarié
        df_resume = df_resultats.groupby("Nom", as_index=False)[["CP N-1", "CP N"]].sum()

        st.subheader("📊 Résumé global par salarié")
        st.dataframe(df_resume, use_container_width=True)

        st.subheader("🔍 Détails individuels")
        nom_selectionne = st.selectbox("Choisissez un salarié :", df_resultats["Nom"].unique())

        df_detail = df_resultats[df_resultats["Nom"] == nom_selectionne]
        st.dataframe(df_detail[["Page", "Libellé", "CP N-1", "CP N"]].sort_values("Page"), use_container_width=True)

    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
else:
    st.info("Veuillez importer un fichier Excel contenant les données de congés générées par votre script PDF.")
