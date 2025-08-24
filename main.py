# OLD VERSION
'''
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

    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "Profile Picture"

    # Menu lateral
    with st.sidebar:
    st.title("Menu")

    if st.button("Profile Picture"):
        st.session_state["pagina"] = "Profile Picture"

    if st.button("Thumbnail Reels"):
        st.session_state["pagina"] = "Thumbnail Reels"

    # Paginas

    if st.session_state["pagina"] == "Profile Picture":
            st.subheader("Download Profile Picture")
            usuario = st.text_input(label="usuario", placeholder="usuário sem @", label_visibility="collapsed")
            if usuario:
                arquivo = download_pfp(usuario)
                with open(arquivo, "rb") as f:
                    st.download_button("Download PFP", f, file_name=arquivo)
                os.remove(arquivo)

    elif st.session_state["pagina"] == "Thumbnail Reels":
            st.subheader("Download Thumbnail Reels")
            usuario = st.text_input(label="url", placeholder="reels url", label_visibility="collapsed")
            if usuario:
                arquivo = download_pfp(usuario)
                with open(arquivo, "rb") as f:
                    st.download_button("Download Thumbnail", f, file_name=arquivo)
                os.remove(arquivo) '''