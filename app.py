import streamlit as st
from st_pages import show_pages, Page, Section

st.set_page_config(page_title="PFP/Thumb Downloader", layout="wide", page_icon="🖼️")

# With sections for better organization
show_pages([
    Page("app.py", "Home", "🏠"),
    
    Section("Download Tools", "📥"),
    Page("profile_picture.py", "Profile Picture", "👤"),
    Page("thumbnail_reels.py", "Instagram Reels", "📸"),
    Page("thumbnail_tiktok.py", "TikTok", "📱"),
])

st.title("Social Media Downloader")
st.write("Navigate using the sidebar menu →")