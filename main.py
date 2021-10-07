from search_algorithms import selection_sort, insertion_sort, merge_sort, shell_sort
import random
import matplotlib.pyplot as plt
import time


def generate_randint_array(power):
    """Generate an array of integers sorted in ascending order."""
    A = []
    for k in range((2**power)+1):
        A.append(random.randint(-1000000, 1000000))

    return A


def generate_ascending_array(power):
    """Generate an array of integers sorted in ascending order."""
    A = []
    for k in range((2**power)+1):
        A.append(random.randint(-1000000, 1000000))

    return sorted(A)


def generate_descending_array(power):
    """Generate an array of integers sorted in descending order."""
    A = []
    for k in range((2**power)+1):
        A.append(random.randint(-1000000, 1000000))

    a = sorted(A)

    return a[:-1]


def generate_triples(power):
    """Generate an array of 1, 2, 3."""
    A = []
    for k in range((2**power)+1):
        A.append(random.randint(1, 3))

    return A


def perform_experiment(arr, repetitions):
    """Perform an experiment by calling each sorting algorithm on a given array.
    Returns time taken by each algorithm."""
    S, M, H, I = 0, 0, 0, 0

    for i in range(repetitions):
        start = time.time_ns()
        c_num1 = insertion_sort(arr)
        I += time.time_ns() - start

        start = time.time_ns()
        c_num2 = selection_sort(arr)
        S += time.time_ns() - start

        start = time.time_ns()
        c_num3 = merge_sort(arr)[1]
        M += time.time_ns() - start

        start = time.time_ns()
        c_num4 = shell_sort(arr)
        H += time.time_ns() - start

    return [I/repetitions, S/repetitions, M/repetitions, H/repetitions, c_num1, c_num2, c_num3, c_num4]


def create_plot(timings, title, option):
    """Function for plotting 2 graphs for an experiment."""
    data = [[], [], [], [], [], [], [], []]
    x_axis = [7, 8, 9, 10, 11, 12, 13, 14, 15]

    for el in timings:
        for i in range(len(el)):
            data[i].append(el[i])

    labels = ["Insertion", "Selection", "Merge", "Shell"]

    if option == "C":
        for i in range(4, 8):
            plt.plot(x_axis, data[i], label=labels[i-4])

    if option == "T":
        for i in range(4):
            plt.plot(x_axis, data[i], label=labels[i])

    plt.yscale("log")
    plt.title(title)
    plt.legend()
    plt.show()
    plt.savefig(title + ".png")


if __name__ == "__main__":
    times_1, times_2, times_3, times_4 = [], [], [], []
    # random integers experiment
    for pow in range(7, 16):
        array = generate_randint_array(pow)
        result = perform_experiment(array, 5)
        times_1.append(result)

    create_plot(times_1, "Random integers experiment", "C")
    create_plot(times_1, "Random integers experiment", "T")
    print(times_1)

    # ascending order experiment
    for pow in range(7, 16):
        array = generate_ascending_array(pow)
        result = perform_experiment(array, 1)
        times_2.append(result)

    create_plot(times_2, "Asccending order experiment", "C")
    create_plot(times_2, "Ascending order experiment", "T")

    # descending order experiment
    for pow in range(7, 16):
        array = generate_descending_array(pow)
        result = perform_experiment(array, 1)
        times_3.append(result)

    create_plot(times_3, "Descending order experiment", "C")
    create_plot(times_3, "Descending order experiment", "T")

    # 1,2,3-only experiment
    for pow in range(7, 16):
        array = generate_triples(pow)
        random.shuffle(array)
        result = perform_experiment(array, 3)
        times_4.append(result)

    create_plot(times_4, "{1, 2, 3} only experiment", "C")
    create_plot(times_4, "{1, 2, 3} only experiment", "T")
