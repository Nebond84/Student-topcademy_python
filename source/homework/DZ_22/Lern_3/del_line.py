def del_line(file_1,file_2):


    with open(file_1,"r",encoding="utf-8") as f1:
        lines = f1.readlines()

        if lines:
            lines = lines[:-1]

    with open(file_2,"w",encoding="utf-8") as f2:
        f2.writelines(lines)






def main():
    file_1 = "Text_files/text.txt"
    file_2 = "Text_files/new_text.txt"
    del_line(file_1,file_2)
if __name__ == "__main__":
    main()