import requests


def challenge17():
    # one hint is cookies
    # second hint is the image - from challenge 4
    # cookies of challenge 4 -> INFO: follow busynothing!!
    # then check the cookies of each page
    fetch_from_internet = False

    info = ''
    if fetch_from_internet:
        nothing = 12345
        uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
        nothing_rep = "and the next busynothing is (\d+)"
        while True:
            try:
                r = requests.get(uri, params={'busynothing': nothing})
                print(r.url)
                info += r.cookies['info']
                print(info)
                content = r.text
                nothing = re.search(nothing_rep, content).group(1)
            except Exception as e:
                break
    else:  # use the info directly
        info = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'

    from urllib.parse import unquote_to_bytes
    res = unquote_to_bytes(info.replace("+", " "))
    import bz2
    print(bz2.decompress(res))  # like challenge 8
    # b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'

    # from challenge13
    import xmlrpc.client # for python 3.x
    conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    print(conn.phone('Leopold'))  # Mozart's father
    # 555-VIOLIN
    # http://www.pythonchallenge.com/pc/return/violin.html
    # http://www.pythonchallenge.com/pc/stuff/violin.php

    from urllib.parse import quote_plus
    url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
    msg = 'the flowers are on their way'
    cookies = dict(info=quote_plus(msg))
    req = requests.get(url, cookies=cookies)
    print(req.text)
    # http://www.pythonchallenge.com/pc/return/balloons.html


def main():
    challenge17()

if __name__ == '__main__':
    main()