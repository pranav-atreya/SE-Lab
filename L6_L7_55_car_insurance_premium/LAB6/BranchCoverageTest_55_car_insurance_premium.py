
import pytest

from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout,
)


def test_unknown_car_type():
    with pytest.raises(ValueError, match="unknown car type"):
        annual_premium("coupe", 30, 0, False)


def test_driver_below_minimum_age():
    with pytest.raises(ValueError, match="driver too young"):
        annual_premium("sedan", 17, 0, False)


def test_young_driver_with_no_claims_and_anti_theft():
    assert annual_premium("hatchback", 21, 0, True) == 9100


def test_middle_aged_driver_with_one_claim():
    assert annual_premium("sedan", 35, 1, False) == 12000


def test_senior_driver_with_multiple_claims():
    assert annual_premium("suv", 60, 3, True) == 33500


def test_senior_driver_without_anti_theft():
    assert annual_premium("sedan", 65, 2, False) == 14000


def test_negative_claim_free_years():
    with pytest.raises(ValueError, match="invalid years"):
        no_claim_bonus(-1)


def test_no_claim_bonus_five_years():
    assert no_claim_bonus(5) == 50


def test_no_claim_bonus_three_years():
    assert no_claim_bonus(3) == 35


def test_no_claim_bonus_one_year():
    assert no_claim_bonus(1) == 20


def test_no_claim_bonus_zero_years():
    assert no_claim_bonus(0) == 0


def test_negative_damage_cost():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(-1, 20000, 500, False)


def test_negative_deductible():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(100, 20000, -1, False)


def test_total_loss_pays_insured_value():
    assert claim_payout(10000, 20000, 500, True) == 20000


def test_damage_equal_to_deductible():
    assert claim_payout(500, 50000, 500, False) == 0


def test_payout_capped_at_insured_value():
    assert claim_payout(10000, 5000, 1000, False) == 5000


def test_normal_claim_payout():
    assert claim_payout(3000, 10000, 500, False) == 2500
