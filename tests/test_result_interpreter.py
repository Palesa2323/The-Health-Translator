
from services.result_interpreter import interpret_reference_range


def test_result_within_range():
    result = {
        "test_name": "Haemoglobin",
        "result": 12.5,
        "unit": "g/dL",
        "reference_min": 12.0,
        "reference_max": 16.0,
    }

    interpreted = interpret_reference_range(result)

    assert interpreted["range_status"] == "Within the stated range"


def test_result_above_range():
    result = {
        "test_name": "Haemoglobin",
        "result": 17.0,
        "unit": "g/dL",
        "reference_min": 12.0,
        "reference_max": 16.0,
    }

    interpreted = interpret_reference_range(result)

    assert interpreted["range_status"] == "Above the stated range"
