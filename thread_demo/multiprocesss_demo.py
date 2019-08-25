import multiprocessing
import time


def test():
    while True:
        print("111111")


def test2():
    while True:
        print("8888")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=test)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()
