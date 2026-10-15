
import re


NUMBER = r"-?\d+(?:\.\d+)?"

UNIT = r"(?:x\s*10\^\d+/L|%|[A-Za-zµμ]+(?:/[A-Za-zµμ]+)?)"

RESULT_PATTERN = re.compile(
    rf"^\s*"
    rf"(?P<test>[A-Za-z][A-Za-z0-9 /()_-]*?)"
    rf"\s+"
    rf"(?P<value>{NUMBER})"
    rf"\s*"
    rf"(?P<unit>{UNIT})"
    rf"\s+"
    rf"(?P<minimum>{NUMBER})"
    rf"\s*[-–]\s*"
    rf"(?P<maximum>{NUMBER})"
    rf"\s*"
    rf"(?P<reference_unit>{UNIT})?"
    rf"\s*$",
    re.IGNORECASE,
)


def parse_results(report_text: str) -> list[dict]:
    """Extract candidate laboratory results for human verification."""

    results = []

    for line_number, line in enumerate(report_text.splitlines(), start=1):
        line = line.strip()

        if not line:
            continue

        match = RESULT_PATTERN.match(line)

        if not match:
            continue

        minimum = float(match.group("minimum"))
        maximum = float(match.group("maximum"))

        if minimum > maximum:
            continue

        unit = match.group("unit").strip()
        reference_unit = match.group("reference_unit")

        if reference_unit:
            normalised_unit = re.sub(r"\s+", "", unit).casefold()
            normalised_reference_unit = re.sub(
                r"\s+", "", reference_unit
            ).casefold()

            if normalised_unit != normalised_reference_unit:
                continue

        results.append(
            {
                "test_name": match.group("test").strip(),
                "result": float(match.group("value")),
                "unit": unit,
                "reference_min": minimum,
                "reference_max": maximum,
                "source_line": line_number,
                "needs_review": True,
            }
        )

    return results
