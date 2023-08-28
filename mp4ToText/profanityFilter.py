from better_profanity import profanity

if __name__ == "__main__":
    profanity.load_censor_words()

    with open("test6.txt", "r") as file:
        content = file.read()
        censored_text = profanity.censor(content)
        print(censored_text)    