

import streamlit as st

from UI.styles import load_styles
from UI.layout import render_home_page
from UI.upload_page import render_upload_section

def main():
    """Configure and launch The Health Translator."""

    st.set_page_config(
        page_title="The Health Translator",
        page_icon="HT",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    load_styles()
    render_home_page()
    st.divider()
    render_upload_section()


if __name__ == "__main__":
    main()
