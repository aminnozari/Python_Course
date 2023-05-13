import os
def load_words(filename):
    words = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                words.append({'english':parts[0], 'persian':parts[1]})
    else:
        print(f"Error: Word bank file {filename} does not exist.")
    return words
def save_words(filename, words):
    with open(filename, 'w') as file:
        for word in words:
            file.write(f"{word['english']},{word['persian']}\n")
def add_word(words):
    english = input("Enter the English word: ")
    persian = input("Enter the Persian translation: ")
    words.append({'english':english, 'persian':persian})
    save_words('word_bank.txt', words)
    print("added to the word bank.")
def translate_to_persian(words, input_string):
    output_string = ""
    sentences = input_string.split('.')
    for sentence in sentences:
        words_list = sentence.strip().split()
        for i in range(len(words_list)):
            found = False
            for word in words:
                if word['english'].lower() == words_list[i].lower():
                    words_list[i] = word['persian']
                    found = True
                    break
            if not found:
                words_list[i] = "*" + words_list[i] + "*"
        output_string += " ".join(words_list) + ". "
    return output_string
def translate_to_english(words, input_string):
    output_string = ""
    sentences = input_string.split('.')
    for sentence in sentences:
        words_list = sentence.strip().split()
        for i in range(len(words_list)):
            found = False
            for word in words:
                if word['persian'].lower() == words_list[i].lower():
                    words_list[i] = word['english']
                    found = True
                    break
            if not found:
                words_list[i] = "*" + words_list[i] + "*"
        output_string += " ".join(words_list) + ". "
    return output_string
word_bank_file = 'word_bank.txt'
words = load_words(word_bank_file)
while True:
    print("\nTranslator Program")
    print("1. Add new word")
    print("2. Translation: English to Persian")
    print("3. Translation: Persian to English")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_word(words)
    elif choice == "2":
        input_string = input("Enter the English text to translate: ")
        output_string = translate_to_persian(words, input_string)
        print("Translated text:", output_string)
    elif choice == "3":
        input_string = input("Enter the Persian text to translate: ")
        output_string = translate_to_english(words, input_string)
        print("Translated text:", output_string)
    elif choice == "4":
        break
    else:
        print("Invalid choice, please try again.")