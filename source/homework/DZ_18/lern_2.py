
def find_reserved_words(text,list_of_words):
    """
    Ищет и выводит зарезервированные слова, присутствующие в тексте.

    :param text: Исходный текст
    :param list_of_words: Список зарезервированных слов
    """
    word_in_text = text.lower().split()

    found_word=set()
    for word in word_in_text:
        if word in list_of_words:
            found_word.add(word)

    if found_word:

        print(f"Совпали слова: {','.join(found_word).upper()}")
    else:
        print(f"Совпадений не найдено!")

text = input(f"Введите текст: ")
list_input = input(f"Введите список зарезервированных слов, через запятую:  ")


# Преобразуем строку в список слов
list_of_words= [word.strip().lower() for word in list_input.split(",")]

find_reserved_words(text,list_of_words)