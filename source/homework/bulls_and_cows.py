import random
from tabnanny import check


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

def check(nums, true_nums):
    bulls = 0
    cows = 0
    for i, num in enumerate(nums):
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows




def del_bad_answers():
    pass


answers = get_all_answer()
player = input_number()
enemy = get_one_answer(answers)

a, b = check(player,enemy)

print(a, b)