
import streamlit as st
from services.document_reader import extract_text
from services.result_parser import parse_results

ALLOWED_FILE_TYPES = ["pdf", "png", "jpg", "jpeg"]


def render_upload_section():
    """Display the report upload and manual-entry options."""

    st.header("Start with your laboratory report")
    st.write(
        "Upload a report or enter your results manually. "
        "You will be able to review the information before "
        "any explanations are generated."
    )

    upload_tab, manual_tab = st.tabs(
        ["Upload a report", "Enter results manually"]
    )

    with upload_tab:
        uploaded_file = st.file_uploader(
            "Choose your laboratory report",
            type=ALLOWED_FILE_TYPES,
            help="Supported formats: PDF, PNG and JPG.",
            key="lab_report_upload",
        )

        if uploaded_file is not None:
            st.success("File uploaded successfully.")
            st.write(f"**Filename:** {uploaded_file.name}")
            st.write(
                f"**File size:** "
                f"{uploaded_file.size / 1024:.1f} KB"
            )

            if st.button(
                "Extract report text",
                key="extract_report_text",
            ):
                with st.spinner("Reading your report..."):
                    extraction = extract_text(uploaded_file)

                st.session_state["report_extraction"] = extraction

            extraction = st.session_state.get("report_extraction")

            if extraction:
                if extraction["success"]:
                    st.success(extraction["message"])

                    st.text_area(
                        "Extracted text - please verify",
                        value=extraction["text"],
                        height=250,
                        key="extracted_report_text",
                    )
                else:
                    st.warning(extraction["message"])

                    if st.button(
                        "Identify possible lab results",
                        key="parse_report_results",
                    ):
                        extracted_text = st.session_state.get(
                            "extracted_report_text",
                            extraction["text"],
                        )

                        parsed_results = parse_results(
                            extracted_text
                        )

                        st.session_state["parsed_results"] = (
                            parsed_results
                        )

                    parsed_results = st.session_state.get(
                        "parsed_results", []
                    )

                    if parsed_results:
                        st.subheader(
                            "Possible results - verify before continuing"
                        )

                        st.warning(
                            "These are automatically extracted candidates. "
                            "Compare every field with the original report."
                        )

                        st.dataframe(
                            parsed_results,
                            use_container_width=True,
                            hide_index=True,
                        )
                    elif "parsed_results" in st.session_state:
                        st.info(
                            "No results matched the current parser. "
                            "This does not mean your report contains "
                            "no laboratory results. You can enter "
                            "them manually."
                        )


    with manual_tab:
        st.caption(
            "Use fictional results while we develop and test "
            "the application."
        )

        with st.form("manual_results_form"):
            test_name = st.text_input(
                "Test name",
                placeholder="e.g. Haemoglobin",
            )

            col1, col2 = st.columns(2)

            with col1:
                result = st.text_input(
                    "Result value",
                    placeholder="e.g. 13.5",
                )

                unit = st.text_input(
                    "Unit",
                    placeholder="e.g. g/dL",
                )

            with col2:
                reference_min = st.text_input(
                    "Reference range minimum",
                    placeholder="e.g. 12.0",
                )

                reference_max = st.text_input(
                    "Reference range maximum",
                    placeholder="e.g. 16.0",
                )

            submitted = st.form_submit_button(
                "Add result",
                use_container_width=True,
            )

        if submitted:
            if not all(
                [
                    test_name.strip(),
                    result.strip(),
                    unit.strip(),
                    reference_min.strip(),
                    reference_max.strip(),
                ]
            ):
                st.error("Please complete all five fields.")

            else:
                try:
                    result_value = float(result)
                    minimum = float(reference_min)
                    maximum = float(reference_max)

                    if minimum > maximum:
                        st.error(
                            "The minimum reference value "
                            "cannot exceed the maximum."
                        )

                    else:
                        new_result = {
                            "test_name": test_name.strip(),
                            "result": result_value,
                            "unit": unit.strip(),
                            "reference_min": minimum,
                            "reference_max": maximum,
                        }

                        st.session_state.setdefault(
                            "lab_results", []
                        )

                        st.session_state.lab_results.append(
                            new_result
                        )

                        st.success(
                            f"{test_name.strip()} added for review."
                        )

                except ValueError:
                    st.error(
                        "Enter numeric values for the result "
                        "and both reference limits."
                    )

        existing_results = st.session_state.get(
            "lab_results", []
        )

        if existing_results:
            st.subheader("Results entered in this session")

            st.dataframe(
                existing_results,
                use_container_width=True,
                hide_index=True,
            )

            if st.button("Clear entered results"):
                st.session_state.lab_results = []
                st.rerun()
