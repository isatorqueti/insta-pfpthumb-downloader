import streamlit as st
import requests
import instaloader
import os

# Função pra baixar a pfp
def download_pfp(usuario):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, usuario)
    url_imagem = profile.profile_pic_url
    imagem = requests.get(url_imagem).content
    nome_arquivo = f"{usuario}_pfp.jpg"
    with open(nome_arquivo, "wb") as f:
        f.write(imagem)
    return nome_arquivo


# Web com Streamlit
st.title("Instagram Downloader")

usuario = st.text_input("Digite o @ do perfil")

if usuario:
    arquivo = download_pfp(usuario)
    with open(arquivo, "rb") as f:
        st.download_button("Download foto de perfil", f, file_name=arquivo)
    os.remove(arquivo)