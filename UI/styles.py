
def load_styles():
    """Apply the application's visual theme."""

    import streamlit as st

    st.markdown(
        """
        <style>
        :root {
            --page-bg: #F7F3FA;
            --surface: #FFFFFF;
            --violet: #76638F;
            --lilac: #C9B5D8;
            --peach: #E6A78D;
            --charcoal: #34303C;
            --muted: #77717F;
        }

        .stApp {
            background: var(--page-bg);
            color: var(--charcoal);
        }

        .block-container {
            max-width: 1120px;
            padding-top: 2.5rem;
            padding-bottom: 4rem;
        }

        h1, h2, h3 {
            color: var(--charcoal);
            letter-spacing: -0.035em;
        }

        .brand-label {
            color: var(--violet);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }

        .hero {
            background: linear-gradient(
                125deg, #FFFFFF 0%, #F0E7F6 72%, #F9E9E1 100%
            );
            border: 1px solid #E5D9ED;
            border-radius: 24px;
            padding: 2.4rem;
            margin: 1rem 0 1.5rem 0;
        }

        .hero h1 {
            font-size: clamp(2.2rem, 5vw, 3.5rem);
            line-height: 1.08;
            margin: 0.7rem 0 1rem 0;
        }

        .hero p {
            color: #625B6B;
            font-size: 1.05rem;
            line-height: 1.75;
            max-width: 680px;
        }

        .feature-card {
            background: var(--surface);
            border: 1px solid #E8E0ED;
            border-radius: 18px;
            padding: 1.25rem;
            min-height: 175px;
        }

        .feature-card h3 {
            font-size: 1.05rem;
            margin-bottom: 0.5rem;
        }

        .feature-card p {
            color: var(--muted);
            font-size: 0.92rem;
            line-height: 1.6;
        }

        .soft-note {
            background: #EFE7F5;
            border-left: 4px solid var(--violet);
            border-radius: 8px;
            padding: 1rem 1.2rem;
            color: var(--charcoal);
            line-height: 1.6;
        }

        div.stButton > button {
            background: var(--violet);
            color: white;
            border: 1px solid var(--violet);
            border-radius: 12px;
            padding: 0.65rem 1.1rem;
            font-weight: 600;
        }

        div.stButton > button:hover {
            background: #655078;
            border-color: #655078;
            color: white;
        }

        [data-testid="stFileUploader"] {
            background: #FFFFFF;
            border: 1px dashed #B9A5CC;
            border-radius: 16px;
            padding: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
