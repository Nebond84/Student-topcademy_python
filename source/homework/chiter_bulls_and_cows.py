import bulls_and_cows

answers = bulls_and_cows.get_all_answer()
counter = 0
while len(answers) > 1:
    counter += 1
    print(f"Ход номер - {counter}")
    print(f"Возможных вариантов ответа: {len(answers)}")
    ans = bulls_and_cows.get_one_answer(answers)
    print(f"Назови комбинацию - {ans}")
    bulls = int(input(f"Сколько быков?:  "))
    cows = int(input(f"Сколько коров?:  "))
    answers = bulls_and_cows.del_bad_answers(answers, ans, bulls, cows)
print(f"Ответ: {answers}")