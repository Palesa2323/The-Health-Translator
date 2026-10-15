
import streamlit as st

from UI.report_upload import render_report_upload
from UI.manual_entry import render_manual_entry
from UI.results_review import render_results_review
from UI.explanation_page import render_explanation_page

def render_upload_section():
    """Display upload and manual-entry workflows separately."""

    st.header("Start with your laboratory report")
    st.write(
        "Upload a report or enter your results manually. "
        "Review the information before receiving explanations."
    )

    upload_tab, manual_tab = st.tabs(
        ["Upload a report", "Enter results manually"]
    )
    
    render_explanation_page()
    
    with upload_tab:
        render_report_upload()

        # Review results extracted from the uploaded report.
        if st.session_state.get("parsed_results"):
            render_results_review(source="upload")

    with manual_tab:
        render_manual_entry()

        # Review results entered manually.
        if st.session_state.get("lab_results"):
            render_results_review(source="manual")
