import re
from validate_docbr import CPF

def is_invalid_name(name):
    return len(name) < 3 or not all(char.isalpha() or char.isspace() for char in name)


def is_invalid_email(email):
    return '@' not in email or '.' not in email.split('@')[-1]


def is_invalid_phone(phone):
    # return len(phone) != 11 or not phone.isdigit()
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, phone)
    return not response


def is_invalid_cpf(cpf_participant):
    cpf = CPF()
    valid_cpf = cpf.validate(cpf_participant)
    return not valid_cpf


