import re


def main():
    ret = re.match(r"^hello+", "hellword")
    if ret:
        print(ret.group())
    else:
        print("无法匹配")


if __name__ == '__main__':
    main()
