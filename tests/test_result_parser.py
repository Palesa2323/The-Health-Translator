
from services.result_parser import parse_results


def test_parse_simple_lab_result():
    report = "Haemoglobin 13.5 g/dL 12.0 - 16.0"

    results = parse_results(report)

    assert len(results) == 1
    assert results[0]["test_name"] == "Haemoglobin"
    assert results[0]["result"] == 13.5
    assert results[0]["unit"] == "g/dL"
    assert results[0]["reference_min"] == 12.0
    assert results[0]["reference_max"] == 16.0


def test_unrecognised_text_is_not_guessed():
    report = "Some unreadable laboratory text"

    assert parse_results(report) == []
