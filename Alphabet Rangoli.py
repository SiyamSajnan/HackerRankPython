from string import ascii_lowercase

def print_rangoli(size):
    # your code goes here

    dash = "-"

    for i in range(size, 0, -1):
        print(dash * ((i * 2) - 2), end="")
        for j in range(size, i, -1):
            print (ascii_lowercase[j - 1] + "-", end="")
        for j in range(i, size + 1):
            if(j != size):
                print (ascii_lowercase[j - 1] + "-", end="")
            else:
                print(ascii_lowercase[j - 1], end="")

        print(dash * ((i * 2) - 2))

    nDash = 2
    for i in range(2, size + 1):
        print(dash * nDash, end="")
        for j in range(size, i, -1):
            print (ascii_lowercase[j - 1] + "-", end="")
        for j in range(i, size + 1):
            if (j != size):
                print(ascii_lowercase[j - 1] + "-", end="")
            else:
                print(ascii_lowercase[j - 1], end="")
        print(dash * nDash)
        nDash += 2


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)