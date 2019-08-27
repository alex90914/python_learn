from urllib import request

'''最简单的爬虫'''
if __name__ == '__main__':
    page = request.urlopen('https://www.dreamatach.com')
    html_code = page.read()
    f = open('e:/a.html', 'wb')
    f.write(html_code)
    print(html_code)
