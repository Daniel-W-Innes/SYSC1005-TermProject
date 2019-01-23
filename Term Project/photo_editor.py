from filters import *


def get_image():
    """
    None -> (Cimpl.Image)

    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.

    >>> image = get_image()
    >>> show(image)

    :return image:
    """
    file = choose_file()
    if file == "":
        sys.exit("File Open cancelled, exiting program")
    img = load_image(file)
    return img


def get_number(text, prompt, i):
    """
    (String,int) -> int

    get a number for use by the filter by look for
    number after the filters command in the user's input or
    prompting the user using text provided.

    >>> image = load_image(choose_file())
    >>> text = str.lower(input())
    >>> number = get_number(text, "Threshold?: "), 0)
    >>> detect_edges_better(image, number)
    >>> show(image)

    :param text:
    :param prompt:
    :param i:
    :return:
    """
    number = 0
    i2 = i
    i3 = i
    c2 = True
    while c2:
        try:
            i2 = i2 + 1
            number = int(str(number) + text[i2])
        except (ValueError, IndexError):
            c2 = False
    try:
        i3 = i3 + 1
        int(text[i3])
    except (ValueError, IndexError):
        number = int(input(prompt))
    return number


def photo_editor(user_input=None, image=None):
    """
    (String and Cimpl.Image) -> None or Cimpl.Image

    a text basted photo editor that runs commands provided by the user on a image

    >>> image = load_image(choose_file())
    >>> text = str.lower(input())
    >>> image = photo_editor(text,image)
    >>> show(image)

    :param user_input:
    :param image:
    :return Cimpl.Image:
    """
    if image is not None:
        image = copy(image)
    c = True
    while c:
        if __name__ == "__main__":
            user_input = str.lower(input("L)oad image \nN)egative G)rayscale X)treme contrast B)lur"
                                         " S)epia tint E)dge detect W)eighted_grayscale O)solarize P)osterize"
                                         "\nI)show image R)eturn image\nQ)uit \n\nExample: lne10iq (not case sensitive)"
                                         " This loads a image takes the negative, runs a edge detection with"
                                         " a threshold of 10, displays the resulting image, and quits\n"))
        else:
            c = False
        for i in range(len(user_input)):
            if user_input[i] == 'l':
                image = get_image()
            elif user_input[i] == 'q':
                c = False
            elif image is not None:
                if user_input[i] == 'n':
                    negative(image)
                elif user_input[i] == 'g':
                    grayscale(image)
                elif user_input[i] == 'x':
                    extreme_contrast(image)
                elif user_input[i] == 'w':
                    weighted_grayscale(image)
                elif user_input[i] == 'b':
                    image = make_very_blurry(image, get_number(user_input, "Number of blurs?: ", i))
                elif user_input[i] == 's':
                    sepia_tint(image)
                elif user_input[i] == 'o':
                    solarize(image, get_number(user_input, "Threshold?: ", i))
                elif user_input[i] == 'e':
                    detect_edges_better(image, get_number(user_input, "Threshold?: ", i))
                elif user_input[i] == 'p':
                        posterize(image, get_number(user_input, "Number of groups?: ", i))
                elif user_input[i] == 'i':
                    show(image)
                elif user_input[i] == 'r':
                    return image
                else:
                    try:
                        int(user_input[i])
                    except ValueError:
                        print("No such command")
            else:
                print("No image loaded")


if __name__ == "__main__":
    photo_editor()
