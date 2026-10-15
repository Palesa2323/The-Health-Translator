from pathlib import Path

import streamlit as st

from UI.styles import load_styles
from UI.layout import render_home_page
from UI.upload_page import render_upload_section


PROJECT_ROOT = Path(__file__).resolve().parent
LOGO_PATH = PROJECT_ROOT / "assets" / "logo.png"


def main():
    """Configure and launch The Health Translator."""

    page_icon = str(LOGO_PATH) if LOGO_PATH.exists() else "🧬"

    st.set_page_config(
        page_title="The Health Translator",
        page_icon=page_icon,
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    load_styles()

    # Keep the logo available in the sidebar.
    with st.sidebar:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), width=140)

        st.caption("Medical language, made human.")

    # Restore the original single-page workflow.
    render_home_page()

    st.divider()

    render_upload_section()


if __name__ == "__main__":
    main()