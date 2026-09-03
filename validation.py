def is_valid_phone(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10


def is_valid_email(email):
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    return (
        username != ""
        and domain != ""
        and "." in domain
        and not username.startswith(".")
        and not username.endswith(".")
        and not domain.startswith(".")
        and not domain.endswith(".")
    )


def is_valid_age(age):
    return age.isdigit() and int(age) > 0


def is_valid_name(name):
    return name.replace(" ", "").isalpha()
