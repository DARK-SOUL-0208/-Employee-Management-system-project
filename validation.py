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
        if age >= 18 and age <= 70:
            return True
        return False
    except ValueError:
        return False
def validate_gender(gender):
    gender = gender.strip().lower()
    if gender == "male" or gender == "female" or gender == "other":
        return True
    return False
def validate_text(text):
    text = text.strip()
    if text == "":
        return False
    for character in text:
        if not (character.isalpha() or character.isspace()):
            return False
    return True
def validate_phone(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    return False
def validate_email(email):
    email = email.strip()
    if "@" in email and "." in email:
        return True
    return False
def validate_salary(salary):
    try:
        salary = float(salary)
        if salary >= 0:
            return True
        return False
    except ValueError:
        return False
