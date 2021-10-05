from search_algorithms import selection_sort, insertion_sort, merge_sort, shell_sort
import random
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
        start = time.time()
        c_num1 = insertion_sort(arr)
        I += time.time() - start

        start = time.time()
        c_num2 = selection_sort(arr)
        S += time.time() - start

        start = time.time()
        c_num3 = merge_sort(arr)[1]
        M += time.time() - start

        start = time.time()
        c_num4 = shell_sort(arr)
        H += time.time() - start
                
    return [[I/repetitions, c_num1], [S/repetitions, c_num2], [M/repetitions, c_num3], [H/repetitions, c_num4]]


if __name__ == "__main__":
    #random integers experiment
    times_1, times_2, times_3, times_4 = [], [], [], []
    for pow in range(7, 16):
        array = generate_randint_array(pow)
        result = perform_experiment(array, 5)
        times_1.append([pow, result])

    print(times_1, end="\n")

    #ascending order experiment
    for pow in range(7, 16):
        array = generate_ascending_array(pow)
        result = perform_experiment(array, 1)
        times_2.append([pow, result])
    
    print(times_2, end="\n")

    #descending order experiment
    for pow in range(7, 12):
        array = generate_descending_array(pow)
        result = perform_experiment(array, 1)
        times_3.append([pow, result])

    print(times_3, end="\n")

    #1,2,3-only experiment
    for pow in range(7, 12):
        array = generate_triples(pow)
        random.shuffle(array)
        result = perform_experiment(array, 3)
        times_4.append([pow, result])
            
    print(times_4)
