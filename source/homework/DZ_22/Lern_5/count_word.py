def count_word(file,input_word):
    with open(file,"r",encoding="utf-8") as f1:
        lines = f1.readlines()
        count = 0
        for line in lines:
            line = line.lower()
            words = line.split()
            count += words.count(input_word.lower())
    return count


def main():
    file = "Text_files/Text.txt"
    input_word = input(f"Введите искомое слово: ")
    res = count_word(file,input_word)
    print(f"Слово '{input_word}' в файле {file} встречается {res} раз(а)")
if __name__ == "__main__":
    main()