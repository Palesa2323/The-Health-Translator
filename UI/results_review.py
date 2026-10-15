import streamlit as st

def render_results_review():
    """Let users review and correct the extracted or manually entered results before proceeding."""
    
    results = st.session_state.get("parsed_results", [])
    
    if not results:
        return
    
    st.divider()
    st.subheader("Review your results")
    
    st.warning(
        "Please verify every field against your original report "
        "These extracted results have not been verified for accuracy."
    )
    
    reviewed_results = []

    for index, item in enumerate(results):
        with st.expander(
            f"{item['test_name']} - Check result",
            expanded=True,
        ):
            test_name = st.text_input(
                "Test name",
                value=item["test_name"],
                key=f"review_test_name_{index}",
            )

            result_value = st.number_input(
                "Result value",
                value=float(item["result"]),
                key=f"review_result_{index}",
            )

            unit = st.text_input(
                "Unit",
                value=item["unit"],
                key=f"review_unit_{index}",
            )

            col1, col2 = st.columns(2)

            with col1:
                minimum = st.number_input(
                    "Reference range minimum",
                    value=float(item["reference_min"]),
                    key=f"review_min_{index}",
                )

            with col2:
                maximum = st.number_input(
                    "Reference range maximum",
                    value=float(item["reference_max"]),
                    key=f"review_max_{index}",
                )

            confirmed = st.checkbox(
                "I have checked these details against the original report",
                key=f"review_confirmed_{index}",
            )

            reviewed_results.append(
                {
                    "test_name": test_name.strip(),
                    "result": result_value,
                    "unit": unit.strip(),
                    "reference_min": minimum,
                    "reference_max": maximum,
                    "verified": confirmed,
                    "needs_review": not confirmed,
                }
            )