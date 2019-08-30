import re


def a():
    ret = re.match(r'(?imx)', 'i')
    print(ret.group())


def main():
    a()


if __name__ == '__main__':
    main()
