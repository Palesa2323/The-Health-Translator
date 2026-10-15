
import json

from google import genai


MODEL_NAME = "gemini-3.8-flash"


def generate_explanations(results: list[dict], api_key: str) -> str:
    """Generate cautious, plain-language explanations for lab results."""

    if not results:
        raise ValueError("No laboratory results were provided.")

    client = genai.Client(api_key=api_key)

    # Send only the fields needed for an explanation.
    safe_results = [
        {
            "test_name": item["test_name"],
            "result": item["result"],
            "unit": item["unit"],
            "reference_min": item["reference_min"],
            "reference_max": item["reference_max"],
        }
        for item in results
    ]

    prompt = f"""
You are a cautious health education assistant for an app
called The Health Translator.

Explain laboratory terminology in clear, simple language.

Rules:
- Do not diagnose diseases or claim that someone has a condition.
- Do not prescribe treatment or recommend changing medication.
- Do not invent missing values, units, or reference ranges.
- Treat the supplied laboratory reference ranges as the source
  for range comparisons. Do not replace them with assumed ranges.
- Explain that results must be considered alongside symptoms,
  medical history, and advice from a qualified healthcare professional.
- If the available information is insufficient, say so clearly.
- Suggest useful questions the person could ask their clinician.
- Use a calm, non-alarming tone.
- Clearly distinguish general educational information from
  conclusions that cannot be drawn from these results.

For each test, provide:
1. What the test measures.
2. What the supplied result and reference range show.
3. What cannot be concluded from this result alone.
4. A useful question to ask a healthcare professional.

Laboratory results:
{json.dumps(safe_results, indent=2)}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    explanation = response.text

    if not explanation:
        raise RuntimeError("The AI returned an empty explanation.")

    return explanation
