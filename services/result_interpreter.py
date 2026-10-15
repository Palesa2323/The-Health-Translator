
def interpret_reference_range(result: dict) -> dict:
    """Compare a numeric result with its supplied reference range."""

    value = result["result"]
    minimum = result["reference_min"]
    maximum = result["reference_max"]

    if minimum > maximum:
        return {
            **result,
            "range_status": "Needs review",
            "range_message": "The reference range is invalid.",
        }

    if value < minimum:
        status = "Below the stated range"
        message = (
            "This result is below the reference range "
            "provided by the laboratory."
        )
    elif value > maximum:
        status = "Above the stated range"
        message = (
            "This result is above the reference range "
            "provided by the laboratory."
        )
    else:
        status = "Within the stated range"
        message = (
            "This result falls within the reference range "
            "provided by the laboratory."
        )

    return {
        **result,
        "range_status": status,
        "range_message": message,
    }
