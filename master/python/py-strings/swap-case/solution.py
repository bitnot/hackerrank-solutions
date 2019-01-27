def swap_case(s):
    return "".join([x.upper() if 'a' <= x <= 'z' else x.lower() for x in s])

