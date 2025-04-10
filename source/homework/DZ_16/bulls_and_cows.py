import random

STRONG = 5040

def get_all_answer():
    """
    Функция создает список возможных вариантов уникальных чисел.
    :return: Возвращает список уникальных чисел
    """
    ans = []
    for  i in range(10000):
        temp = str(i).zfill(4)
        # через множества проверяем уникальность чисел
        if len(set(map(int, temp))) == 4:
            ans.append(list(map(int, temp)))
        # через генератор списков проверяем уникальность чисел
        # lst = ["x" for num in temp if temp.count(num) == 1]
        # if len(lst) == 4:
        #     ans.append(list(map(int, temp)))
    return ans



def get_one_answer(ans):
    """
    Функция генерирует случайное число из списка возможных вариантов.
    :param ans: Принимает список созданный ранее
    :return: возвращает случайно выбранное число.
    """
    num = random.choice(ans)
    return num


def input_number():
    while True:
        nums  = input(f"Введите четыре неповторяющиеся цифры: ")
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums

def check_nums(nums, true_nums):
    bulls = 0
    cows = 0
    for i, num in enumerate(nums):
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows



def del_bad_answers(ans, enemy_try, bull, cow):
    i = 0
    for num in ans[:]:
        i += 1
        temp_bull, temp_cow = check_nums(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
        if i > STRONG:
            break
    return ans


def main():

    print(f"Игра 'Быки и коровы'")

    answers = get_all_answer()
    player = input_number()
    enemy = get_one_answer(answers)

    while True:
        print("=" * 15 ,"Ход игрока", "=" * 15)
        print(f"Угадайте число компьютера")
        number = input_number()
        bulls, cows = check_nums(number, enemy)
        print(f"Быки: {bulls}, Коровы: {cows}")
        if bulls == 4:
            print(f"Победил игрок, число компьютера: {enemy}")
            break

        print("=" * 15, "Ход компьютера", "=" * 15)
        enemy_try = get_one_answer(answers)
        print(f"компьютер считает что вы загадали число: {enemy_try}")
        bulls, cows = check_nums(enemy_try, player)
        print(f"Быки: {bulls}, Коровы: {cows}")
        if bulls == 4:
            print(f"Победил компьютер, число компьютера: {enemy}")
            break
        else:
            answers = del_bad_answers(answers,enemy_try,bulls,cows)

if __name__ == "__main__":
    STRONG = 10
    main()