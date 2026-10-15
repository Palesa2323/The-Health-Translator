
import streamlit as st

from ui.report_upload import render_report_upload
from ui.manual_entry import render_manual_entry


def render_upload_section():
    st.header("Start with your laboratory report")
    st.write(
        "Upload a report or enter your results manually. "
        "Review the information before any explanations "
        "are generated."
    )

    upload_tab, manual_tab = st.tabs(
        ["Upload a report", "Enter results manually"]
    )

    with upload_tab:
        render_report_upload()

    with manual_tab:
        render_manual_entry()
