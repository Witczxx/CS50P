def main():
    inpt = str(input("Input: "))
    outpt = omit(inpt)
    print(f"Output: {outpt}")

def omit(txt):
    small_vocals = "aeiou"
    big_vocals = "AEIOU"

    for numb in range(len(small_vocals)):
        new_txt = txt.replace(small_vocals[numb], "")
        txt = new_txt
    else:
        pass

    for numb in range(len(big_vocals)):
        new_txt = txt.replace(big_vocals[numb], "")
        txt = new_txt
    else:
        pass
    
    return txt

main()