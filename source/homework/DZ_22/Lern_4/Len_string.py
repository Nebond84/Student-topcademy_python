def len_string(file):
    with open(file,"r",encoding="utf-8") as f1:
        lines = f1.readlines()
        long_line = ""
        max_length = 0
        for line in lines:
            current_length = len(line)
            if current_length > max_length:
                max_length = current_length - 1
                long_line = line
    return (f"{max_length} символов\n\n"
            f"\tСамая длинная строка:\n\n\t{long_line}")





def main():
    file = "Text_files/Text_1.txt"
    res = len_string(file)
    print(f"\n\tДлинна самой длинной строки в файле - {file}, составляет - {res} ")

if __name__ == "__main__":
    main()