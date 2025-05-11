def statistics_text(file_1,file_2):
    vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU")
    consonants = set("бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    digits = set("0123456789")

    with open(file_1,"r",encoding="utf-8") as f1:
        lines = f1.readlines()

    num_lines = len(lines)
    num_chars = 0
    num_vowels = 0
    num_consonants = 0
    num_digits = 0

    for line in lines:
        num_chars += len(line)
        for char in line:
            if char in vowels:
                num_vowels += 1
            elif char in consonants:
                num_consonants += 1
            elif char in digits:
                num_digits += 1

    with open(file_2,"w",encoding="utf-8") as f2:
        f2.write(f"Статистика по файлу {file_1}:\n")
        f2.write(f"\tКоличество символов: {num_chars}\n")
        f2.write(f"\tКоличество строк: {num_lines}\n")
        f2.write(f"\tКоличество гласных: {num_vowels}\n")
        f2.write(f"\tКоличество согласных: {num_consonants}\n")
        f2.write(f"\tКоличество цифр: {num_digits}\n")





def main():
    file_1 = "Text_files/text_1.txt"
    file_2 = "Text_files/statistic.txt"
    statistics_text(file_1,file_2)
if __name__ == "__main__":
    main()


