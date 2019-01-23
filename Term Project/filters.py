from Cimpl import *


def grayscale(image):
    """
    (Cimpl.Image) -> None

    Convert image into shades of gray.

    >>> image = load_image(choose_file())
    >>> grayscale(image)
    >>> show(image)

    :param image:
    :return:
    """
    for x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.

        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def weighted_grayscale(image):
    """
    (Cimpl.Image) -> None

    Convert image into shades of gray.

    >>> image = load_image(choose_file())
    >>> weighted_grayscale(image)
    >>> show(image)

    :param image:
    :return:
    """
    for x, y, (r, g, b) in image:
        # Use the shade of gray that has the same brightness as the pixel's
        # original color.

        brightness = r * 0.299 + g * 0.587 + b * 0.114
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)


def solarize(image, threshold=200):
    """
    (Cimpl.Image, int) -> None

    Solarize image, modifying the RGB components that
    have intensities that are less than threshold.
    Parameter threshold is in the range 0 to 256, inclusive.

    >>> image = load_image(choose_file())
    >>> solarize(image)
    >>> show(image)

    :param image:
    :param threshold:
    :return:
    """
    for x, y, (r, g, b) in image:

        if r < threshold:
            r = 255 - r

        if g < threshold:
            g = 255 - g

        if b < threshold:
            b = 255 - b

        solarized = create_color(r, g, b)
        set_color(image, x, y, solarized)


def negative(image):
    """ (Cimpl.Image) -> None
    >>> image = load_image(choose_file())
    >>> negative(image)
    >>> show(image)
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(255-r, 255-g, 255-b))


def black_and_white(image):
    """
    (Cimpl.Image) -> None

    Convert image to a black-and-white (two-tone) image.

    >>> image = load_image(choose_file())
    >>> black_and_white(image)
    >>> show(image)

    :param image:
    :return:
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on
    # whether its brightness is in the lower or upper half of this range.

    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3

        if brightness < 128:
            set_color(image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(image, x, y, white)


def extreme_contrast(image):
    """
    (Cimpl.Image) -> None

    Modify image, maximizing the contrast between the light
    and dark pixels.

    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    >>> show(image)

    :param image:
    :return:
    """
    for x, y, (r, g, b) in image:
        if r < 128:
            r = 0
        else:
            r = 255
        if g < 128:
            g = 0
        else:
            g = 255
        if b < 128:
            b = 0
        else:
            b = 255
        set_color(image, x, y, create_color(r, g, b))


def black_and_white_and_gray(image):
    """
    (Cimpl.Image) -> None

    Convert image to a black-and-white-and-gray (three-tone) image.

    >>> image = load_image(choose_file())
    >>> black_and_white_and_gray(image)
    >>> show(image)

    :param image:
    :return:
    """
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3

        if brightness < 85:
            set_color(image, x, y, black)
        elif brightness < 171:  # brightness is between 85 and 170, inclusive
            set_color(image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(image, x, y, white)


def sepia_tint(image):
    """
    (Cimpl.Image) -> None

    Convert image to sepia tones.

    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)

    :param image:
    :return:
    """
    grayscale(image)
    for x, y, (r, g, b) in image:
        if r < 63:
            b = b * 0.9
            r = r * 1.1
        elif r < 192:
            b = b * 0.85
            r = r * 1.15
        else:
            b = b * 0.93
            r = r * 1.08
        set_color(image, x, y, create_color(r, g, b))


def _adjust_component_old(amount):
    """
    (int) -> int

    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.

    >>> _adjust_component_old(10)
    31
    >>> _adjust_component_old(85)
    95
    >>> _adjust_component_old(142)
    159
    >>> _adjust_component_old(230)
    223

    :param amount:
    :return midpoint:
    """
    if amount <= 63:
        return 31
    elif amount <= 127:
        return 95
    elif amount <= 191:
        return 159
    else:
        return 223


def posterize_old(image):
    """
    (Cimpl.Image) -> None

    "Posterize" the specified image.

    >>> image = load_image(choose_file())
    >>> posterize_old(image)
    >>> show(image)

    :param image:
    :return:
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(
            _adjust_component_old(r),
            _adjust_component_old(g),
            _adjust_component_old(b)))


def _adjust_component(amount, number_of_groups=4):
    """
    (int) -> int

    Divide the range 0..255 into n equal-size groups,
    and return the midpoint of the groups in which the
    specified amount lies.

    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223

    :param amount:
    :return midpoint:
    """
    for i in range(0, number_of_groups):
        if amount <= 255 / number_of_groups + 255 / number_of_groups * i:
            return int(255 / number_of_groups + 255 / number_of_groups * (i - 1) + 255 / number_of_groups / 2)


def posterize(image, number_of_groups=4):
    """
    (Cimpl.Image) -> None

    "Posterize" the specified image.

    >>> image = load_image(choose_file())
    >>> posterize(image)
    >>> show(image)

    :param image:
    :param number_of_groups:
    :return:
    """
    for x, y, (r, g, b) in image:
        set_color(image, x, y, create_color(_adjust_component(r, number_of_groups),
                                            _adjust_component(g, number_of_groups),
                                            _adjust_component(b, number_of_groups)))


def difference(pict_1, pict_2):
    """
    (Cimpl.Image) -> (Cimpl.Image)

    Find the difference between two images of the same size and return as a images

    >>> show(difference(load_image(choose_file()), load_image(choose_file())))

    :param pict_1:
    :param pict_2:
    :return difference:
    """
    if get_width(pict_1) == get_width(pict_2) and get_height(pict_1) == get_height(pict_2):
        difference = create_image(get_width(pict_1), get_height(pict_1))
        for x, y, (r, g, b) in pict_1:
            r2, g2, b2 = get_color(pict_2, x, y)
            set_color(difference, x, y, create_color(r-r2, g-g2, b-b2))
        return difference
    return False


def blur(image):
    """
    (Cimpl.Image) -> (Cimpl.Image)

    Return a new image that is a blurred copy of source.

    >>> original = load_image(choose_file())
    >>> blurred = blur(original)
    >>> show(blurred)

    :param image:
    :return blurred:
    """
    blurred = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            top_right_red, top_right_green, top_right_blue = get_color(image, x + 1, y - 1)
            top_red, top_green, top_blue = get_color(image, x, y - 1)
            top_left_red, top_left_green, top_left_blue = get_color(image, x - 1, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_right_red, bottom_right_green, bottom_right_blue = get_color(image, x + 1, y + 1)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            bottom_left_red, bottom_left_green, bottom_left_blue = get_color(image, x + 1, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            new_red = (top_right_red + top_red + top_left_red + left_red + bottom_right_red + bottom_red +
                       bottom_left_red + right_red + center_red) // 9
            new_green = (top_right_green + top_green + top_left_green + left_green + bottom_right_green +
                         bottom_green + bottom_left_green + right_green + center_green) // 9
            new_blue = (top_right_blue + top_blue + top_left_blue + left_blue + bottom_right_blue + bottom_blue +
                        bottom_left_blue + right_blue + center_blue) // 9
            new_color = create_color(new_red, new_green, new_blue)
            set_color(blurred, x, y, new_color)
    return blurred


def make_very_blurry(image, number_of_blurs=10):
    """
    (Cimpl.Image) -> (Cimpl.Image)

    Return a new image that is a blurred copy of source, passing through a blurr filter n times.

    >>> image = load_image(choose_file())
    >>> image = make_very_blurry(image, 100)
    >>> show(image)

    :param image:
    :param number_of_blurs:
    :return blurred:
    """
    blurred = copy(image)
    for i in range(number_of_blurs):
        blurred = blur(image)
    return blurred


def detect_edges(image, threshold=3):
    """
    (Cimpl.Image) -> None

    Modify image using edge detection.

    >>> image = load_image(choose_file())
    >>> detect_edges(image)
    >>> show(image)

    :param image:
    :param threshold:
    :return :
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image)):
            r, g, b = get_color(image, x, y)
            r2, g2, b2 = get_color(image, x, y + 1)
            if abs((r + g + b) // 3 - (r2 + g2 + b2) // 3) > threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)


def detect_edges_better(image, threshold=3):
    """
    (Cimpl.Image) -> None

    Modify image using a improved edge detection.

    :param image:
    :param threshold:
    :return :
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    for y in range(0, get_height(image) - 1):
        for x in range(0, get_width(image) - 1):
            r, g, b = get_color(image, x, y)
            rdown, gdown, bdown = get_color(image, x, y + 1)
            rright, gright, bright = get_color(image, x + 1, y)
            if abs((r + g + b) // 3 - (rdown + gdown + bdown) // 3) > threshold or \
                    abs((r + g + b) // 3 - (rright + gright + bright) // 3) > threshold:
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)
