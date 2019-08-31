def set_fun(fun):
    def call_fun(*args, **kwargs):
        print("1111111111111")
        return_data = fun(*args, **kwargs)
        print("22222222222")
        return return_data

    return call_fun


@set_fun
def test(num, *args, **kwargs):
    print("---num----->", num)
    print("---args----->", args)
    print("----kwargs---->", kwargs)
    return "xxxxxx"


if __name__ == '__main__':
    # test(100)
    # print()
    # test(100, 200)
    rest = test(100, 200, mn=91)
    print(rest)
