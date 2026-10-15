
import streamlit as st

from services.medical_explainer import generate_explanations


def render_explanation_page():
    """Display AI-generated educational explanations for verified results."""

    results = st.session_state.get("verified_results", [])

    if not results:
        return

    st.divider()
    st.header("Understand your results")

    st.write(
        "Get a plain-language explanation of your laboratory results, "
        "including what each test measures and questions to discuss "
        "with your healthcare professional."
    )

    st.warning(
        "This feature provides general health education, not a diagnosis. "
        "It does not replace advice from a qualified healthcare professional."
    )

    if st.button(
        "Explain my results",
        key="generate_explanations",
        use_container_width=True,
    ):
        try:
            api_key = st.secrets["GEMINI_API_KEY"]

            with st.spinner("Preparing your explanations..."):
                explanation = generate_explanations(
                    results=results,
                    api_key=api_key,
                )

            st.session_state["ai_explanation"] = explanation

        except KeyError:
            st.error(
                "The API key was not found. Check your "
                ".streamlit/secrets.toml configuration."
            )

        except Exception as error:
            print(
                f"AI explanation error: "
                f"{type(error).__name__}: {error}"
            )

            st.error(
                "We couldn't generate an explanation right now."
            )
            st.caption(
                f"Error type: {type(error).__name__}. "
                "Check the VS Code terminal for details."
            )

    explanation = st.session_state.get("ai_explanation")

    if explanation:
        st.subheader("Your explanation")
        st.markdown(explanation)
