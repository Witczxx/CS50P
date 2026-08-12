import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    pattern = r"(^[0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3}$)"
    match = re.search(pattern, ip)
    if match:
        matches = [match.group(1), match.group(2), match.group(3), match.group(4)]
        for ip_bit in matches:
            if int(ip_bit) <= 255:
                pass
            else:
                return "False."
        return "True."
    else:
        return "False."

if __name__ == "__main__":
    main()
