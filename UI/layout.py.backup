
import streamlit as st


def render_header():
    """Display the application's brand and introduction."""

    st.markdown(
        """
        <div class="brand-label">THE HEALTH TRANSLATOR</div>

        <section class="hero">
            <div class="brand-label">YOUR RESULTS, EXPLAINED</div>
            <h1>Medical language,<br>made human.</h1>
            <p>
                Understand your laboratory reports without getting
                lost in complicated medical terminology. Explore
                what your results mean, what the reference ranges
                show, and what you may want to ask your clinician.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_features():
    """Explain the main capabilities of the application."""

    st.subheader("A clearer way to understand your results")

    first, second, third = st.columns(3)

    features = [
        (
            "01",
            "Upload your report",
            "Start with a PDF or image of your laboratory report, "
            "or enter results manually.",
        ),
        (
            "02",
            "Understand the details",
            "Explore test terminology, units, and the reference "
            "ranges supplied by your laboratory.",
        ),
        (
            "03",
            "Prepare for your next step",
            "Get plain-language explanations and useful questions "
            "to discuss with your healthcare professional.",
        ),
    ]

    for column, (number, heading, description) in zip(
        (first, second, third), features
    ):
        with column:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="brand-label">{number}</div>
                    <h3>{heading}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_safety_note():
    """Explain the intended use and limitations."""

    st.markdown(
        """
        <div class="soft-note">
            <strong>Designed to inform, not diagnose.</strong>
            This tool helps explain medical terminology. It cannot
            diagnose a condition or determine your overall health.
            Discuss your results with a qualified healthcare
            professional, even when values fall within a stated range.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_home_page():
    """Assemble the landing page from its individual sections."""

    render_header()
    render_features()

    st.write("")
    render_safety_note()

    st.write("")
    st.subheader("Ready to explore a report?")
    st.write(
        "The report upload and manual-entry workflow will be "
        "added next. For now, this is the foundation of the interface."
    )
