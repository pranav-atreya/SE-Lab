
import pytest

from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout,
)


def test_annual_premium_young_driver_no_claims_with_anti_theft():
    # Hatchback: 8000 + 4000 age surcharge
    # 20% no-claim reduction, followed by anti-theft discount
    assert annual_premium("hatchback", 21, 0, True) == 9100


def test_annual_premium_senior_driver_multiple_claims():
    # SUV: 15000 + 2000 age surcharge, doubled for 3 claims,
    # then reduced by the anti-theft discount
    assert annual_premium("suv", 60, 3, True) == 33500


def test_annual_premium_unknown_car_type():
    with pytest.raises(ValueError, match="unknown car type"):
        annual_premium("coupe", 35, 0, True)


def test_annual_premium_driver_too_young():
    with pytest.raises(ValueError, match="driver too young"):
        annual_premium("sedan", 17, 0, True)


def test_no_claim_bonus_invalid_years():
    with pytest.raises(ValueError, match="invalid years"):
        no_claim_bonus(-1)


def test_no_claim_bonus_five_or_more_years():
    assert no_claim_bonus(5) == 50


def test_no_claim_bonus_three_years():
    assert no_claim_bonus(3) == 35


def test_no_claim_bonus_one_year():
    assert no_claim_bonus(1) == 20


def test_no_claim_bonus_zero_years():
    assert no_claim_bonus(0) == 0


def test_claim_payout_negative_damage():
    with pytest.raises(ValueError, match="invalid amount"):
        claim_payout(-1, 20000, 500, False)


def test_claim_payout_total_loss():
    assert claim_payout(10000, 20000, 500, True) == 20000


def test_claim_payout_damage_within_deductible():
    assert claim_payout(500, 50000, 500, False) == 0


def test_claim_payout_capped_at_insured_value():
    assert claim_payout(10000, 5000, 1000, False) == 5000


def test_claim_payout_normal_case():
    assert claim_payout(3000, 10000, 500, False) == 2500
