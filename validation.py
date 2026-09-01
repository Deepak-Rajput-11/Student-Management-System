def is_valid_phone(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10


def is_valid_email(email):
    return (
        "@" in email
        and "." in email
        and not email.startswith("@")
        and not email.endswith(".")
        and email.index("@") < email.rindex(".")
    )


def is_valid_age(age):
    return age.isdigit() and int(age) > 0


def is_valid_name(name):
    return name.replace(" ", "").isalpha()
