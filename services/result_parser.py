
import re


def parse_results(report_text: str) -> list[dict]:
    """Identify possible laboratory results in extracted text.

    This first version recognises simple rows containing:
    test name, numeric result, unit, and reference range.
    It does not diagnose or interpret medical meaning.
    """

    results = []

    pattern = re.compile(
        r"(?P<test>[A-Za-z][A-Za-z /()-]{1,50}?)\s+"
        r"(?P<value>-?\d+(?:\.\d+)?)\s+"
        r"(?P<unit>[A-Za-z%µμ/^.0-9]+)\s+"
        r"(?P<minimum>-?\d+(?:\.\d+)?)\s*[-–]\s*"
        r"(?P<maximum>-?\d+(?:\.\d+)?)"
    )

    for line in report_text.splitlines():
        match = pattern.search(line.strip())

        if not match:
            continue

        minimum = float(match.group("minimum"))
        maximum = float(match.group("maximum"))

        if minimum > maximum:
            continue

        results.append(
            {
                "test_name": match.group("test").strip(),
                "result": float(match.group("value")),
                "unit": match.group("unit"),
                "reference_min": minimum,
                "reference_max": maximum,
                "needs_review": False,
            }
        )

    return results
