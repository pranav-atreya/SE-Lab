from hypothesis import given, strategies as st

from car_insurance_premium_parser import (
    normalize_registration,
    total_claim_amount,
    driver_age,
)


@given(st.text() | st.none())
def test_normalize_registration_no_crash(value):
    try:
        normalize_registration(value)
    except Exception as exc:
        assert False, f"normalize_registration crashed with {type(exc).__name__}: {exc}"


@given(st.text() | st.none())
def test_total_claim_amount_no_crash(value):
    try:
        total_claim_amount(value)
    except Exception as exc:
        assert False, f"total_claim_amount crashed with {type(exc).__name__}: {exc}"


@given(st.text() | st.none())
def test_driver_age_no_crash(value):
    try:
        driver_age(value)
    except Exception as exc:
        assert False, f"driver_age crashed with {type(exc).__name__}: {exc}"
