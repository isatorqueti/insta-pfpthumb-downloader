import streamlit as st
import os
from utils import download_pfp  # supondo que você tenha essa função num arquivo utils.py

def main():
    st.title("Instagram Downloader")
    st.subheader("Download Profile Picture")
    usuario = st.text_input(label="usuario", placeholder="usuário sem @", label_visibility="collapsed")
    
    if usuario:
        arquivo = download_pfp(usuario)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(arquivo, caption="Preview", width=280)
            with open(arquivo, "rb") as f:
                st.download_button("Download PFP", f, file_name=arquivo, use_container_width=True)
            os.remove(arquivo)

if __name__ == "__main__":
    main()