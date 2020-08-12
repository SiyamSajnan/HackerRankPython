import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width);

    newStr = wrapper.wrap(string)
    toReturn = ""

    for element in newStr:
        if element == newStr[0]:
            toReturn = element
        else:
            toReturn = toReturn + "\n" + element

    return toReturn


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
