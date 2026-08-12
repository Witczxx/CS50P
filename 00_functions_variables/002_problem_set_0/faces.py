def str_convert(org):
    org = str(org)
    return org.replace(":)", "🙂").replace(":(", "🙁")

print(str_convert(input()))