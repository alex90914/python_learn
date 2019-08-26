from concurrent.futures import ThreadPoolExecutor
import time


def say(age):
    while True:
        print(age)
        time.sleep(2)


def drink(age):
    while True:
        print(age)
        time.sleep(2)


def main():
    pool = ThreadPoolExecutor(3)
    pool.submit(say, (2,))
    pool.submit(drink, (1,))


if __name__ == '__main__':
    main()
