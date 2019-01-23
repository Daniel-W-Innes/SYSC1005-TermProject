from Cimpl import *


def filter_b(img, h):
    """
    >>> img = load_image(choose_file())
    >>> filter_b(img,50)
    >>> show(img)

    :param img:
    :param h:
    :return:
    """
    black = create_color(0, 0, 0)
    for x, y, (r, g, b) in img:
        if y <= h or y >= get_height(img) - h:
            set_color(img, x, y, black)
        else:
            set_color(img, x, y, create_color(r * 0.7, g * 0.7, b * 0.7))


def filter_d(img):
    """
    >>> img = load_image(choose_file())
    >>> filter_d(img)

    :param img:
    :return:
    """
    d = {}
    for x, y, (r, g, b) in img:
        br = (r + g + b) / 3
        d[br] = d.get(br, 0) + 1
    bmax = max(d)
    bmin = min(d)
    print('The brightest pixel has a brightness of ', bmax)
    print('There are ', d[bmax], ' brightest pixels')
    print('The darkest pixel has a brightness of ', bmin)
    print('There are ', d[bmin], ' darkest pixels')


def fun(s,e):
    """

    >>> print(fun(2,4))

    :param s:
    :param e:
    :return:
    """
    d = {}
    for num in range(s, e+1):
        d[num] = num**2
    return d

inv={}
inv['chest']={'g':50,'s':75,'d':1}

