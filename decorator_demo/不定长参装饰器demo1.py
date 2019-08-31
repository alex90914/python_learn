def set_fun(fun):
    def call_fun(*args, **kwargs):
        print("1111111111111")
        fun(*args, **kwargs)
        print("22222222222")

    return call_fun


@set_fun
def test(num, *args, **kwargs):
    print("---num----->", num)
    print("---args----->", args)
    print("----kwargs---->", kwargs)


if __name__ == '__main__':
    # test(100)
    # print()
    # test(100, 200)
    test(100, 200, mn=91)
