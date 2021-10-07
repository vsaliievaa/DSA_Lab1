"""sorting algorithms"""


def merge(lst1: list, lst2: list) -> list:
    """Returns two lists merged into one."""
    counter = 0
    new_list = []
    one, two = 0, 0
    while one != len(lst1) and two != len(lst2):
        if lst1[one] <= lst2[two]:
            new_list.append(lst1[one])
            one += 1
        else:
            new_list.append(lst2[two])
            two += 1
        counter += 1
    new_list.extend(lst1[one:])
    new_list.extend(lst2[two:])
    return (new_list, counter)


def merge_sort(lst: list) -> list:
    """Merge Sort implementation."""
    counter = 0
    result = []
    lst_copy = lst
    for i in range(len(lst_copy)):
        result.append([lst_copy[i]])

    i = 0
    while i < len(result)-1:
        lst1 = result[i]
        lst2 = result[i+1]
        new_list, num = (merge(lst1, lst2))
        counter += num
        result.append(new_list)
        i += 2
    if len(result) != 0:
        lst_copy[:] = result[-1][:]
    return (lst_copy, counter)


def selection_sort(lst: list) -> list:
    """Selection Sort implementation."""
    length = len(lst)
    counter = 0
    lst_copy = lst
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            counter += 1
            if lst_copy[min_index] > lst_copy[j]:

                min_index = j
        lst_copy[i], lst_copy[min_index] = lst_copy[min_index], lst_copy[i]
    return counter


def insertion_sort(lst: list) -> list:
    """Insertion Sort implementation."""
    length = len(lst)
    lst_copy, counter = lst, 0
    for i in range(1, length):
        curr_element = lst_copy[i]
        idx = i-1
        if not (lst_copy[idx] > curr_element and idx >= 0):
            counter += 1
        else:
            while lst_copy[idx] > curr_element and idx >= 0:
                counter += 1
                lst_copy[idx+1] = lst_copy[idx]
                idx -= 1
            if idx >= 0:
                counter += 1
        lst_copy[idx+1] = curr_element

    return counter


def shell_sort(lst: list):
    """Shell sort implementation."""
    counter = 0
    lst_copy = lst
    length = len(lst_copy)
    interval = length // 2
    while interval > 0:
        for i in range(interval, length):
            temp = lst_copy[i]
            j = i
            counter += 1
            while j >= interval and lst_copy[j-interval] > temp:
                if lst_copy[j-interval] > temp:
                    counter += 1
                    lst_copy[j], lst_copy[j -
                                          interval] = lst_copy[j-interval], lst_copy[j]
                    j -= interval
                else:
                    break

            lst_copy[j] = temp
        interval = interval // 2

    return counter
