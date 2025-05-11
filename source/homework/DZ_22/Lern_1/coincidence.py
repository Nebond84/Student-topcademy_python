def compare_files(file_1,file_2):
    with open(file_1,"r",encoding = "utf-8") as f1, open(file_2,"r", encoding="utf-8") as f2:
        lines_1 = f1.readlines()
        lines_2 = f2.readlines()


    lines_1 = [line.strip() for line in lines_1]
    lines_2 = [line.strip() for line in lines_2]


    min_length = min(len(lines_1),len(lines_2))

    for i in range(min_length):
        if lines_1[i] != lines_2[i]:
            print(f"Несовпадающая строка из {file_1} (строка{i+1}): {lines_1[i]}\n")
            print(f"Несовпадающая строка из {file_2} (строка{i + 1}): {lines_2[i]}\n")

    if len(lines_1) > min_length:
        for i in range(min_length,len(lines_1)):
            print(f"Дополнительная строка из {file_1} (строка {i + 1}): {lines_1[i]}\n")

    if len(lines_2) > min_length:
        for i in range(min_length, len(lines_2)):
            print(f"Дополнительная строка из {file_2} (строка {i + 1}): {lines_2[i]}")


def main():
    file_1 = "Text_files/text_1.txt"
    file_2 = "Text_files/text_2.txt"

    compare_files(file_1,file_2)

if __name__ == "__main__":
    main()