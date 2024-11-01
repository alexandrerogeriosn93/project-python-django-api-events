def is_invalid_name(name):
    return len(name) < 3 or not all(char.isalpha() or char.isspace() for char in name)


def is_invalid_email(email):
    return '@' not in email or '.' not in email.split('@')[-1]


def is_invalid_phone(phone):
    return len(phone) != 11 or not phone.isdigit()

