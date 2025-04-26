import random

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key

def custom_sort(arr):
    n = len(arr)
    if n == 0:
        return arr
    average = sum(arr) / n
    first_third = n // 3
    two_third = (n * 2) // 3

    first = arr[:first_third]
    second = arr[first_third:two_third]
    remaining = arr[two_third:]

    if average > 0:
        full_to_sort = arr[:two_third]
        insertion_sort(full_to_sort)
        sorted_part = full_to_sort
    else:
        insertion_sort(first)
        sorted_part = first + remaining

    sorted_remaining = list(reversed(remaining))

    result = sorted_part + sorted_remaining

    return result

def main():
    number_list = []
    for i in range(10):
        number_list.append(random.randint(-128, 500))
    print(f"{number_list}")
    sorted_list = custom_sort(number_list)
    print(f"{sorted_list}")
if __name__ == "__main__":
    main()
