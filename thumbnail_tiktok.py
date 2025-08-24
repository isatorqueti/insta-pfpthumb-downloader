import streamlit as st
import os
from utils import download_tiktok_thumbnail

def main():
    st.title("TikTok Downloader")
    st.subheader("Download Thumbnail TikTok")
    url = st.text_input(label="url", placeholder="tiktok url", label_visibility="collapsed")

    if url:
        arquivo, thumb_url = download_tiktok_thumbnail(url)
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(thumb_url, caption="preview", width=280)
            with open(arquivo, "rb") as f:
                st.download_button("Download Thumbnail", f, file_name=arquivo, use_container_width=True)
            os.remove(arquivo)

if __name__ == "__main__":
    main()