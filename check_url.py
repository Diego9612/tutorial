from string import ascii_letters, digits


def check_url(
    string,
):

    # 1. starts with http:// or https://
    # 2. contains at least a dot
    # 3. the part of the string after the last dota
    #    is composed of 2, 3 or 4 alphabetic characters
    # 4. the entire string is composed only of
    #    alphanumeric characters and the symbols
    #    dont, slash, dash, underscore ./-_

    # Examples
    # "example"                   -> False
    # "example.org"               -> False
    # "https://example.org"       -> True
    # "https://my-1.example.org"  -> True
    # "https://ex,ample.org"      -> False
    # "https://example.admin"     -> False

    # 1
    if not (string.startswith("http://") or string.startswith("https://")):
        return False
    # 2
    if "." not in string:
        return False
    # 3
    str_list = string.split(".")
    last_part = str_list[-1]
    if len(last_part) > 4 or len(last_part) < 2:
        return False
    for char in last_part:
        if not char in ascii_letters:
            return False
    # 4
    valid_characters = ascii_letters + digits + "./-_"
    for chat in string:
        if char not in valid_characters:
            return False
    return True


print(check_url("example"))
print(check_url("http://example"))
print(check_url("http://example.it"))
