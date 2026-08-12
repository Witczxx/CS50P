def main():
    inpt = str(input("Input: "))
    outpt = shorten(inpt)
    print(f"Output: {outpt}")


def shorten(word):
    small_vocals = "aeiou"
    big_vocals = "AEIOU"

    for numb in range(len(small_vocals)):
        new_word = word.replace(small_vocals[numb], "")
        word = new_word
    else:
        pass

    for numb in range(len(big_vocals)):
        new_word = word.replace(big_vocals[numb], "")
        word = new_word
    else:
        pass

    return word


if __name__ == "__main__":
    main()
