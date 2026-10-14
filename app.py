
import streamlit as st  # type: ignore[import-not-found]


def main():
    """Start The Health Translator application."""
    st.set_page_config(
        page_title="The Health Translator",
        page_icon="💜",
        layout="wide",
    )

    st.title("The Health Translator")
    st.write("Medical language, made human.")

    st.info(
        "Our application foundation is ready. "
        "The interface and report-processing features will be "
        "implemented in separate modules."
    )


if __name__ == "__main__":
    main()
