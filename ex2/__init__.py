import time

from ex2 import fetcher

CALL_COUNT = 10


def print_results(running_time):
    for i in range(0, len(running_time)):
        print(f'Run {i+1}: {running_time[i]}')
    print(f'Average: {sum(running_time) / len(running_time)}')


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        # put your code here
        def nested_wrapper(*args, **kwargs):
            running_time = []
            for i in range(0, num):
                start = time.time()
                func(*args, **kwargs)
                finish = time.time()
                running_time.append(finish - start)
            print_results(running_time)
        return nested_wrapper
    return wrapper

@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
