def set_fun(fun):
    def call_fun(a):
        print("1111111111111")
        fun(a)
        print("22222222222")

    return call_fun


@set_fun
def test(num):
    print("aaaaaaaaa----->%d" % num)


if __name__ == '__main__':
    a = test(111)
