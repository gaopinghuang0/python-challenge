# -*- coding:utf-8 -*-

import requests, re
from PIL import Image, ImageDraw  # pillow


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


def challenge18():
    # http://www.pythonchallenge.com/pc/return/brightness.html
    # download deltas.gz
    import gzip, difflib
    data = gzip.open("18/deltas.gz")
    d1, d2 = [], []
    for line in data:
        d1.append(line[:53].decode()+'\n')
        d2.append(line[56:].decode())

    compare = difflib.Differ().compare(d1, d2)

    f = open('18/f.png', 'wb')
    f1 = open('18/f1.png', 'wb')
    f2 = open('18/f2.png', 'wb')

    for line in compare:
        # print(line)
        bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
        if bs:
            if line[0] == '+':
                f1.write(bs)
            elif line[0] == '-':
                f2.write(bs)
            else:
                print(bs)
                f.write(bs)

    f.close()   # do not open with Sublime Text. Use windows image viewer.
    f1.close()
    f2.close()
    # ../hex/bin.html
    # butter
    # fly
    # http://www.pythonchallenge.com/pc/hex/bin.html

def challenge19():
    import email, base64, wave

    message = open("19/email.txt", "rb").read().decode()
    mail = email.message_from_string(message)

    audio = mail.get_payload(0).get_payload(decode=True)
    # print(audio)
    with open("19/indian.wav", "wb") as f:
        f.write(audio)



    w = wave.open('19/indian.wav', 'rb')

    h = wave.open("19/result.wav", "wb")

    print(w.getnchannels())
    print(w.getsampwidth())
    print(w.getframerate())
    h.setnchannels(w.getnchannels())
    h.setsampwidth(w.getsampwidth()//2)
    h.setframerate(w.getframerate()*2)
    frames = w.readframes(w.getnframes())
    wave.big_endiana = 1
    h.writeframes(frames)
    print(h.getnchannels())
    print(h.getsampwidth())
    print(h.getframerate())    

    h.close()
    # http://www.pythonchallenge.com/pc/hex/idiot2.html


def challenge20():
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    s = requests.Session()
    s.auth = ('butter', 'fly')
    req = s.get(url)  
    print(req.headers)
    pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
    (start, end, length) = pattern.search(req.headers['Content-Range']).groups()

    while True:
        try:
            s.headers.update({'Range': 'bytes=%i-'%(int(end) + 1)})
            req = s.get(url)
            print(req.headers)
            print(req.text)
            (start, end, length) = pattern.search(req.headers['Content-Range']).groups()
        except:
            break

    # end = 30346
    # invader
    
    # then check the content after the length
    s.headers.update({'Range': 'bytes=%i-'%(int(length) + 1)})
    req = s.get(url)
    print(req.headers)
    print(req.text)
    (start, end, length) = pattern.search(req.headers['Content-Range']).groups()
    # esrever ni emankcin wen ruoy si drowssap eht  --> reverse
    # the password is your new nickname in reverse
    # invader --> redavni  (password)
    # go back
    s.headers.update({'Range': 'bytes=%i-'%(int(start) - 1)})
    req = s.get(url)
    print(req.headers)
    print(req.text)
    # and it is hiding at 1152983631.
    s.headers.update({'Range': 'bytes=1152983631-'})
    req = s.get(url)
    with open('21/question.zip', 'wb') as f:
        f.write(bytes(req.content))  # passwd: redavni
    # level 21 is not a url, but inside this zip file

    
def challenge21():
    import zlib, bz2
    with open('21/question/package.pack', 'rb') as f:
        data = f.read()

        result = ''

        while True:
            if data.startswith(b'x\x9c'):
                data = zlib.decompress(data)
                result += ' '
            elif data.startswith(b'BZh'):
                data = bz2.decompress(data)
                result += '#'
            elif data.endswith(b'\x9cx'):
                data = data[::-1]
                result += '\n'
            else:
                break

        print(data)  # b'sgol ruoy ta kool', add logging
        print(result)  # copper
        # http://www.pythonchallenge.com/pc/hex/copper.html


# completely don't understand
def challenge22():
    img = Image.open('22/white.gif')
    print(img.size)
    new = Image.new("RGB", (500, 200))
    draw = ImageDraw.Draw(new)
    cx, cy = 0, 100
    for frame in range(img.n_frames):
        img.seek(frame)
        left, upper, right, lower = img.getbbox()

        # get the direction; like a joystick, 
        dx = left - 100
        dy = upper - 100

        # end of a move(letter), shift to the right
        if dx == dy == 0:
            cx += 50
            cy = 100
        cx += dx
        cy += dy
        draw.point([cx, cy])

    new.show()
    # bonus
    # http://www.pythonchallenge.com/pc/hex/bonus.html


def challenge23():
    import this
    print(this.s)
    print(this.d)
    s = 'va gur snpr bs jung?'
    print(''.join([this.d.get(c, c) for c in s]))
    # in the face of what? -> ambiguity
    # http://www.pythonchallenge.com/pc/hex/ambiguity.html


def challenge24():
    maze = Image.open('24/maze.png')
    w, h = maze.size
    for i in range(w):
        print(maze.getpixel((i,0)))  # entrance is not white
    for i in range(w):
        print(maze.getpixel((i, h-1)))  # exit is not white
        
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    white = (255, 255, 255, 255)

    next_map = {}

    entrance = (w - 2, 0)
    exit = (1, h - 1)
    queue = [exit]
    while queue:
        pos = queue.pop(0)
        if pos == entrance:
            break
        for d in directions:
            tmp = (pos[0] + d[0], pos[1] + d[1])
            if not tmp in next_map and 0 <= tmp[0] < w and 0 <= tmp[1] < h and maze.getpixel(tmp) != white:
                next_map[tmp] = pos
                queue.append(tmp)

    path = []
    while pos != exit: 
        path.append(maze.getpixel(pos)[0])
        pos = next_map[pos]

    # skipping all 0s
    print(path)
    open('24/maze.zip', 'wb').write(bytes(path[1::2]))
    # lake
    # http://www.pythonchallenge.com/pc/hex/lake.html



def main():
    challenge24()

if __name__ == '__main__':
    main()