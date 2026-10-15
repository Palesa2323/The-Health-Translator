import streamlit as st

from UI.report_upload import render_report_upload
from UI.manual_entry import render_manual_entry
from UI.results_review import render_results_review
from UI.explanation_page import render_explanation_page


def render_upload_section():
    """Display upload and manual-entry workflows separately."""

    st.header("My Report")

    st.write(
        "Upload a laboratory report or enter your results manually. "
        "You will be able to review the information before requesting "
        "an AI explanation."
    )

    upload_tab, manual_tab = st.tabs(
        ["Upload a report", "Enter results manually"]
    )

    with upload_tab:
        render_report_upload()

        if st.session_state.get("parsed_results"):
            render_results_review(source="upload")

    with manual_tab:
        render_manual_entry()

        if st.session_state.get("lab_results"):
            render_results_review(source="manual")
            
        render_explanation_page()