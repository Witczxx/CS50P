def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()

    chapter1 = contents[21:54]
    with open("chapter1.txt", "w") as f:
        # self-made 1-liner : f.write("Chapter I.")
        f.writelines(chapter1)


main()
