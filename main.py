import random
from colored import fore, back, style

TRIES = 10


def get_user_word():
    while True:
        word = input("Enter your guess: ")
        word = word.lower()

        if word.isalpha():
            if len(word) == 5:
                break

            print("Please enter a 5 lettered word\n")
        else:
            print("Please enter a valid word\n")

    return word


def get_random_word():
    with open(
        r"E:\Zairza AI-ML Projects\Python Projects\WordleClone\words.txt",
        "r",
        encoding="utf8",
    ) as word_file:
        words = word_file.readlines()

        for index, value in enumerate(words):
            words[index] = value[:-1]

        random_word = random.choice(words)

        return random_word


def check_word(current_user_word: str, current_random_word: str):
    result_string = ""

    user_word_list = list(current_user_word)
    random_word_list = list(current_random_word)

    # for i, v in enumerate(user_word_list):
    #     letter = v.upper()
    #     user_word_list[i] = letter

    # for i, v in enumerate(random_word_list):
    #     letter = v.upper()
    #     random_word_list[i] = letter

    for i, _ in enumerate(user_word_list):
        if user_word_list[i] == current_random_word[i]:
            result_string += f"{style('bold')}{fore('#ffffff')}{back('green')}{user_word_list[i].upper()}{style('reset')}"
            random_word_list.remove(user_word_list[i])
        else:
            if user_word_list[i] in random_word_list:
                result_string += f"{style('bold')}{fore('#ffffff')}{back('yellow')}{user_word_list[i].upper()}{style('reset')}"
                random_word_list.remove(user_word_list[i])
            else:
                result_string += f"{style('bold')}{fore('#ffffff')}{back('#000000')}{user_word_list[i].upper()}{style('reset')}"

    print(f"\n{result_string}")


def main():
    current_random_word = get_random_word()
    counter = 1

    tries = TRIES

    while True:
        tries -= 1
        user_word = get_user_word()

        if user_word == current_random_word:
            check_word(user_word, current_random_word)
            print(f"You have correctly guessed the word in {counter} tries")
            break

        check_word(user_word, current_random_word)
        print(f"\nNumber of chances remaining: {tries}\n")

        counter += 1

        if tries == 0:
            print(f"The correct word is {current_random_word}")
            print(f"You failed to guess with {TRIES} chances")
            break

    while True:
        choice = input("\nDo you want to play again (Y/n): ").strip()

        if choice == "Y":
            main()
        else:
            break


print(
    f"{style('bold')}{fore('#ffffff')}{back('#000000')}Python Wordle Game{style('reset')}"
)
main()
