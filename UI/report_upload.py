
import streamlit as st

from services.document_reader import extract_text
from services.result_parser import parse_results


ALLOWED_FILE_TYPES = ["pdf", "png", "jpg", "jpeg"]


def render_report_upload():
    uploaded_file = st.file_uploader(
        "Choose your laboratory report",
        type=ALLOWED_FILE_TYPES,
        help="Supported formats: PDF, PNG and JPG.",
        key="lab_report_upload",
    )

    if uploaded_file is None:
        return

    st.success("File uploaded successfully.")
    st.write(f"**Filename:** {uploaded_file.name}")
    st.write(f"**File size:** {uploaded_file.size / 1024:.1f} KB")

    if st.button("Extract report text", key="extract_report_text"):
        with st.spinner("Reading your report..."):
            st.session_state["report_extraction"] = extract_text(
                uploaded_file
            )

        # Clear results from a previous extraction.
        st.session_state.pop("parsed_results", None)

    extraction = st.session_state.get("report_extraction")

    if not extraction:
        return

    if not extraction["success"]:
        st.warning(extraction["message"])
        return

    st.success(extraction["message"])

    st.text_area(
        "Extracted text - please verify",
        value=extraction["text"],
        height=200,
        key="extracted_report_text",
    )

    if st.button(
        "Identify possible lab results",
        key="parse_report_results",
    ):
        text_to_parse = st.session_state.get(
            "extracted_report_text", extraction["text"]
        )

        st.session_state["parsed_results"] = parse_results(
            text_to_parse
        )

    if "parsed_results" in st.session_state:
        results = st.session_state["parsed_results"]

        st.subheader("Possible results")
        st.caption(
            "Verify every field against the original report "
            "before using these results."
        )

        if results:
            st.dataframe(
                results,
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info(
                "No results matched the current parser. "
                "You can enter results manually."
            )
