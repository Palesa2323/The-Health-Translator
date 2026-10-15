
from services.result_parser import parse_results


def test_parse_simple_lab_result():
    results = parse_results(
        "Haemoglobin 13.5 g/dL 12.0 - 16.0"
    )

    assert len(results) == 1
    assert results[0]["test_name"] == "Haemoglobin"
    assert results[0]["result"] == 13.5
    assert results[0]["unit"] == "g/dL"
    assert results[0]["reference_min"] == 12.0
    assert results[0]["reference_max"] == 16.0


def test_parse_all_six_cbc_results():
    report = """
RBC Count 4.2 x 10^12/L 4.5-5.9 x 10^12/L
Hemoglobin (Hgb) 12.5 g/dL 13.8-17.2 g/dL
Hematocrit (Hct) 37.5% 41.0-50.0%
Mean Corpuscular Volume (MCV) 89 fL 80-96 fL
WBC Count 11.5 x 10^9/L 4.0-10.0 x 10^9/L
Platelet Count 280 x 10^9/L 150-450 x 10^9/L
"""

    results = parse_results(report)

    assert len(results) == 6

    assert [item["test_name"] for item in results] == [
        "RBC Count",
        "Hemoglobin (Hgb)",
        "Hematocrit (Hct)",
        "Mean Corpuscular Volume (MCV)",
        "WBC Count",
        "Platelet Count",
    ]

    assert [item["result"] for item in results] == [
        4.2, 12.5, 37.5, 89.0, 11.5, 280.0
    ]

    assert results[0]["unit"] == "x 10^12/L"
    assert results[2]["unit"] == "%"
    assert results[4]["unit"] == "x 10^9/L"

    assert all(item["needs_review"] for item in results)


def test_unrecognised_text_is_not_guessed():
    assert parse_results(
        "Some unreadable laboratory text"
    ) == []


def test_reversed_reference_range_is_rejected():
    assert parse_results(
        "Haemoglobin 13.5 g/dL 16.0-12.0 g/dL"
    ) == []


def test_conflicting_reference_unit_is_rejected():
    assert parse_results(
        "Haemoglobin 13.5 g/dL 12.0-16.0 %"
    ) == []
