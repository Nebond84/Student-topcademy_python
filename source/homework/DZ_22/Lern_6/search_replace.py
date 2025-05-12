def search_replace(input_file, output_file, target, word_rep):
    with open(input_file, "r", encoding="utf-8") as f1:
        content = f1.read()

        new_content = content.replace(target,word_rep)

    with open(output_file,"w",encoding="utf-8") as f2:
        f2.write(new_content)




def main():
    input_file = "Text_files/Text_1.txt"
    output_file = "Text_files/Text_2.txt"
    target = input("Введите искомое слово: ")
    word_rep = input("Введите слово для замены: ")
    search_replace(input_file, output_file, target, word_rep)


if __name__ == "__main__":
    main()
