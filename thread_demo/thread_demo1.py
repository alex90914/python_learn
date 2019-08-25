import threading
import time
import datetime


class ThreadDemo:
    def __init__(self):
        self.name = '这是哪干'

    def say(self):
        self.name = '沾上干'
        print("aaa" + str(datetime.datetime.now()))
        time.sleep(1000)

    def say2(self):
        print("bbbb" + str(datetime.datetime.now()))
        time.sleep(1000)


if __name__ == '__main__':
    say1 = threading.Thread(target=ThreadDemo.say)
    say2 = threading.Thread(target=ThreadDemo.say2)
    print(say1.name)
    print(say2.name)
    say1.start()
    say2.start()

    time.sleep(4)
    #
    # while True:
    #     length = threading.enumerate()
    #     print("%s" % length)
