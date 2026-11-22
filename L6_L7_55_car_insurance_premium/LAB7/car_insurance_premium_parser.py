"""Hardened input parsers for the Lab 7 fuzz-testing exercise."""

from datetime import datetime
import re
from typing import Optional


def normalize_registration(plate):
    """Normalize a registration string; return an empty string for non-text input."""
    if not isinstance(plate, str):
        return ""

    normalized = plate.strip().upper()
    for character in (" ", "-", "."):
        normalized = normalized.replace(character, "")
    return normalized


def total_claim_amount(text):
    """Sum valid non-negative whole-number claims separated by semicolons.

    Empty, malformed, negative, and non-string inputs are ignored safely.
    """
    if not isinstance(text, str):
        return 0

    total = 0
    for raw_amount in text.split(";"):
        amount = raw_amount.strip()
        if not amount or not amount.isdecimal():
            continue

        try:
            total += int(amount)
        except (ValueError, OverflowError):
            # Ignore values that Python cannot safely convert.
            continue

    return total


def driver_age(dob, current_year=2026) -> Optional[int]:
    """Return age in years from a strict DD/MM/YYYY date, or None if invalid.

    As in the supplied starter implementation, the calculation uses only
    current_year and the birth year; it does not account for the birthday
    having occurred yet in the current year.
    """
    if not isinstance(dob, str):
        return None
    if isinstance(current_year, bool) or not isinstance(current_year, int):
        return None
    if current_year < 1 or current_year > 9999:
        return None

    value = dob.strip()
    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", value) is None:
        return None

    try:
        birth_date = datetime.strptime(value, "%d/%m/%Y").date()
    except ValueError:
        return None

    age = current_year - birth_date.year
    if age < 0:
        return None
    return age


def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    print("Normalized registration:", normalize_registration(value))

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    print("Total claimed:", total_claim_amount(value))

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    age = driver_age(value)
    print("Driver age in 2026:", age if age is not None else "Invalid date of birth")


if __name__ == "__main__":
    main()
