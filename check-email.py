import re
from validate_email_address import validate_email
from email.utils import parseaddr

def validate_email_regex(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def validate_email_library(email):
    return validate_email(email)

def validate_email_builtin(email):
    return '@' in parseaddr(email)[1]

def validate_email_all_methods(email):
    is_valid_regex = validate_email_regex(email)
    is_valid_library = validate_email_library(email)
    is_valid_builtin = validate_email_builtin(email)
    
    return all([is_valid_regex, is_valid_library, is_valid_builtin])

# Example
email = "example@test.com"
print(validate_email_all_methods(email)) 
