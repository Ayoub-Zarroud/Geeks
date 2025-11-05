def get_age(year, month, day):
    # Hard-code the current date (for example: November 2025)
    current_year = 2025
    current_month = 11
    current_day = 5

    age = current_year - year

    # Adjust if birthday hasn't happened yet this year
    if (current_month, current_day) < (month, day):
        age -= 1

    return age

def can_retire(gender, date_of_birth):
    # Split the date string into year, month, and day
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)

    # Define retirement ages
    if gender.lower() == 'm':
        retirement_age = 67
    elif gender.lower() == 'f':
        retirement_age = 62
    else:
        print("Invalid gender input. Use 'm' or 'f'.")
        return False

    # Check if the person can retire
    return age >= retirement_age

# === Main Program ===
gender = input("Enter your gender (m/f): ").strip()
date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ").strip()

if can_retire(gender, date_of_birth):
    print("You can retire!")
else:
    print("You cannot retire yet.")
