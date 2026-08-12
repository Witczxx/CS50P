import emoji


def main():
    written_emoji = input("Input: ")
    print(emoji.emojize(written_emoji, language="alias", variant="emoji_type"))


main()
