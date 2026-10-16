
import tomllib
from pathlib import Path

from services.medical_explainer import generate_explanations


secrets_path = Path(".streamlit/secrets.toml")

with secrets_path.open("rb") as file:
    secrets = tomllib.load(file)

api_key = secrets["GEMINI_API_KEY"]

# Fictional laboratory data for testing only.
sample_results = [
    {
        "test_name": "Haemoglobin",
        "result": 13.5,
        "unit": "g/dL",
        "reference_min": 12.0,
        "reference_max": 16.0,
    }
]

try:
    explanation = generate_explanations(
        results=sample_results,
        api_key=api_key,
    )

    print("\nAI CONNECTION SUCCESSFUL\n")
    print(explanation)

except Exception as error:
    print("\nAI CONNECTION FAILED")
    print(f"Error type: {type(error).__name__}")
    print(error)
