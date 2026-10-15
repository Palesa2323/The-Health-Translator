
import streamlit as st


def render_manual_entry():
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
                "Result value", placeholder="e.g. 13.5"
            )
            unit = st.text_input(
                "Unit", placeholder="e.g. g/dL"
            )

        with col2:
            reference_min = st.text_input(
                "Reference range minimum", placeholder="e.g. 12.0"
            )
            reference_max = st.text_input(
                "Reference range maximum", placeholder="e.g. 16.0"
            )

        submitted = st.form_submit_button(
            "Add result", use_container_width=True
        )

    if submitted:
        if not all(
            value.strip()
            for value in [
                test_name, result, unit, reference_min, reference_max
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
                        "The minimum reference value cannot "
                        "exceed the maximum."
                    )
                else:
                    new_result = {
                        "test_name": test_name.strip(),
                        "result": result_value,
                        "unit": unit.strip(),
                        "reference_min": minimum,
                        "reference_max": maximum,
                        "needs_review": True,
                    }

                    st.session_state.setdefault("lab_results", [])
                    st.session_state["lab_results"].append(new_result)

                    st.success(
                        f"{test_name.strip()} added for review."
                    )

            except ValueError:
                st.error(
                    "Enter numeric values for the result "
                    "and both reference limits."
                )

    existing_results = st.session_state.get("lab_results", [])

    if existing_results:
        st.subheader("Results entered in this session")
        st.dataframe(
            existing_results,
            use_container_width=True,
            hide_index=True,
        )

        if st.button("Clear entered results"):
            st.session_state["lab_results"] = []
            st.rerun()
