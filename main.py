import re

def check_password_strength(password: str) -> dict:
    """Return a dictionary with password checks."""
    checks = {
        "length_at_least_8": len(password) >= 8,
        "has_digit": bool(re.search(r"\d", password)),
        "has_uppercase": bool(re.search(r"[A-Z]", password)),
        "has_lowercase": bool(re.search(r"[a-z]", password)),
        "has_special_char": bool(re.search(r"[^\w]", password)),  # non-alphanumeric
    }
    return checks

def print_result(checks: dict):
    all_ok = all(checks.values())

    print("\nPassword strength report:")
    print("-------------------------")
    print(f"Length ≥ 8 characters : {'✅' if checks['length_at_least_8'] else '❌'}")
    print(f"Contains a digit      : {'✅' if checks['has_digit'] else '❌'}")
    print(f"Contains uppercase    : {'✅' if checks['has_uppercase'] else '❌'}")
    print(f"Contains lowercase    : {'✅' if checks['has_lowercase'] else '❌'}")
    print(f"Contains special char : {'✅' if checks['has_special_char'] else '❌'}")

    if all_ok:
        print("\nOverall: ✅ Strong password!")
    else:
        print("\nOverall: ❌ Weak password. Try to meet all the criteria above.")

def main():
    print("🔐 Password Strength Checker")
    print("----------------------------")
    pwd = input("Enter a password to check: ")
    checks = check_password_strength(pwd)
    print_result(checks)

if __name__ == "__main__":
    main()
