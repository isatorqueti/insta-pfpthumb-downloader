import streamlit as st

nav = st.navigation([
    st.Page("pages/profile_picture.py", title="Instagram Profile Picture", icon="👤"),
    st.Page("pages/thumbnail_reels.py", title="Thumbnail Reels", icon="📸"), 
    st.Page("pages/thumbnail_tiktok.py", title="Thumbnail TikTok", icon="🎬")
])

nav.run()