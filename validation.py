def validate_name(name):
    name = name.strip()
    if name == "":
        return False
    for character in name:
        if not (character.isalpha() or character.isspace()):
            return False
    return True
def validate_age(age):
    try:
        age = int(age)
        return 18 <= age <= 70
    except ValueError:
        return False
def validate_gender(gender):
    gender = gender.strip().lower()
    return gender in ["male", "female", "other"]
def validate_text(text):
    text = text.strip()
    if text == "":
        return False
    for character in text:
        if not (character.isalpha() or character.isspace()):
            return False
    return True
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10
def validate_email(email):
    email = email.strip()
    if "@" not in email or "." not in email:
        return False
    return True
def validate_salary(salary):
    try:
        salary = float(salary)
        return salary >= 0
    except ValueError:
        return False