import streamlit as st
import os
from utils import download_thumbnail

def main():
    st.title("Instagram Downloader")
    st.subheader("Download Thumbnail Reels")
    url = st.text_input(label="url", placeholder="reels url", label_visibility="collapsed")

    if url:
        arquivo = download_thumbnail(url)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(arquivo, caption="Preview", width=280)
            with open(arquivo, "rb") as f:
                st.download_button("Download Thumbnail", f, file_name=arquivo, use_container_width=True)
            os.remove(arquivo)

if __name__ == "__main__":
    main()