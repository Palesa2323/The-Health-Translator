
import streamlit as st

from services.medical_explainer import generate_explanations


def main():
    print("Checking Gemini connection...")

    api_key = st.secrets.get("GEMINI_API_KEY")

    if not api_key:
        print("FAILED: GEMINI_API_KEY was not found.")
        return

    sample_results = [
        {
            "test_name": "Haemoglobin",
            "result": 13.5,
            "unit": "g/dL",
            "reference_min": 12.0,
            "reference_max": 16.0,
        },
        {
            "test_name": "White Blood Cell Count",
            "result": 7.2,
            "unit": "x10^9/L",
            "reference_min": 4.0,
            "reference_max": 11.0,
        },
    ]

    try:
        explanation = generate_explanations(
            results=sample_results,
            api_key=api_key,
        )

        print("\nSUCCESS: Gemini returned an explanation.\n")
        print(explanation)

    except Exception as error:
        print(f"\nFAILED: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
