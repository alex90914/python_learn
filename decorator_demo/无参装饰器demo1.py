def set_fun(fun):
    def call_fun():
        print("1111111111111")
        fun()
        print("22222222222")

    return call_fun


@set_fun
def test():
    print("aaaaaaaaa")


test()
