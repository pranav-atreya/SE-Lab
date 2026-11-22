# Lab 6 - Car Insurance Premium

Python implementation of a car insurance premium calculator, tested using pytest to check code coverage and branch coverage.

## Files

| File | Description |
|---|---|
| `car_insurance_premium.py` | Contains the insurance premium, no-claim bonus and claim payout functions. |
| `test_car_insurance_premium.py` | Basic test cases for the application. |
| `CodeCoverageTest_55_car_insurance_premium.py` | Test cases covering the different functions and execution paths. |
| `BranchCoverageTest_55_car_insurance_premium.py` | Test cases covering the conditional branches in the application. |

## Functions

The application contains three main functions:

- `annual_premium()` - Calculates the yearly premium based on car type, driver age, claim history and anti-theft device availability.
- `no_claim_bonus()` - Calculates the no-claim bonus based on the number of claim-free years.
- `claim_payout()` - Calculates the insurance payout based on damage cost, insured value, deductible and total-loss status.

## Running the Tests

Install pytest:

```bash
pip install pytest
```

Run the individual test files:

```bash
python -m pytest -v test_car_insurance_premium.py
python -m pytest -v CodeCoverageTest_55_car_insurance_premium.py
python -m pytest -v BranchCoverageTest_55_car_insurance_premium.py
```

Run all three together:

```bash
python -m pytest -v test_car_insurance_premium.py CodeCoverageTest_55_car_insurance_premium.py BranchCoverageTest_55_car_insurance_premium.py
```
