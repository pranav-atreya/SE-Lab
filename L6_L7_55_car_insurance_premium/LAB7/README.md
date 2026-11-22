# Lab 7 - Fuzz Testing

A Python-based fuzz testing exercise using Hypothesis to find and fix input validation issues in a car insurance premium parser.

The original program assumes that inputs are always valid. Hypothesis is used to generate unexpected inputs and identify cases that cause the application to fail.

## Project Files

| File | Description |
|---|---|
| `car_insurance_premium_parser.py` | Main application containing the three parser functions. |
| `test_car_insurance_premium_parser.py` | Hypothesis tests for the parser functions. |

## Requirements

- Python 3.8 or later
- pytest
- Hypothesis

Install the dependencies:

```bash
pip install hypothesis pytest
```

## Running the Application

```bash
python car_insurance_premium_parser.py
```

## Running the Tests

```bash
python -m pytest -v test_car_insurance_premium_parser.py
```

## Functions Tested

1. **`normalize_registration()`** – Removes spaces, hyphens and periods from registration numbers and converts them to uppercase.
2. **`total_claim_amount()`** – Calculates the total of semicolon-separated claim amounts.
3. **`driver_age()`** – Calculates the driver's age using a date of birth in `DD/MM/YYYY` format.

## Testing

The initial fuzz tests exposed issues with unexpected inputs, including `None` values and empty strings. These failures were used to identify where input validation was missing.

The application was updated to handle invalid inputs safely. After the changes, all three Hypothesis tests passed.
