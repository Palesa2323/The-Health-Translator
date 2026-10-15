
import streamlit as st

from services.result_interpreter import interpret_reference_range


def render_results_review(source="upload"):
    """Review, verify, and interpret candidate laboratory results."""

    if source == "upload":
        results = st.session_state.get("parsed_results", [])
    else:
        results = st.session_state.get("lab_results", [])

    if not results:
        return

    st.divider()
    st.subheader("Review your results")

    st.warning(
        "Check every field against the original report. "
        "These results are not verified until you confirm them."
    )

    reviewed_results = []

    for index, item in enumerate(results):
        test_name_default = str(item.get("test_name", ""))
        unit_default = str(item.get("unit", ""))

        with st.expander(
            f"{test_name_default or 'Unnamed test'} - Check result",
            expanded=True,
        ):
            test_name = st.text_input(
                "Test name",
                value=test_name_default,
                key=f"review_test_name_{index}",
            )

            result_value = st.number_input(
                "Result value",
                value=float(item.get("result", 0.0)),
                key=f"review_result_{index}",
            )

            unit = st.text_input(
                "Unit",
                value=unit_default,
                key=f"review_unit_{index}",
            )

            col1, col2 = st.columns(2)

            with col1:
                minimum = st.number_input(
                    "Reference range minimum",
                    value=float(item.get("reference_min", 0.0)),
                    key=f"review_min_{index}",
                )

            with col2:
                maximum = st.number_input(
                    "Reference range maximum",
                    value=float(item.get("reference_max", 0.0)),
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

    # This button must be OUTSIDE the for loop.
    if st.button(
        "Save reviewed results",
        key="save_reviewed_results",
        use_container_width=True,
    ):
        errors = []

        for index, item in enumerate(reviewed_results):
            if not item["test_name"]:
                errors.append(
                    f"Result {index + 1}: enter a test name."
                )

            if not item["unit"]:
                errors.append(
                    f"Result {index + 1}: enter a unit."
                )

            if item["reference_min"] > item["reference_max"]:
                errors.append(
                    f"Result {index + 1}: the minimum "
                    "cannot exceed the maximum."
                )

            if not item["verified"]:
                errors.append(
                    f"Result {index + 1}: confirm that you "
                    "checked the details against the report."
                )

        if errors:
            for error in errors:
                st.error(error)

        else:
            interpreted_results = [
                interpret_reference_range(item)
                for item in reviewed_results
            ]

            st.session_state["verified_results"] = (
                interpreted_results
            )

            st.success("Reviewed results saved successfully.")
            st.subheader("Your results at a glance")

            for item in interpreted_results:
                st.markdown(f"**{item['test_name']}**")
                st.write(
                    f"Result: {item['result']} {item['unit']}"
                )
                st.write(
                    f"Laboratory reference range: "
                    f"{item['reference_min']}–"
                    f"{item['reference_max']} {item['unit']}"
                )
                st.info(
                    f"{item['range_status']}\n\n"
                    f"{item['range_message']}"
                )

            st.caption(
                "This comparison uses the reference range you supplied. "
                "It is not a diagnosis or a substitute for medical advice."
            )
