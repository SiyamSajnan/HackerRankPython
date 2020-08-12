def print_formatted(number):
    # your code goes here

    a = len(str(bin(number))[2:])

    for j in range(1, number + 1):

        octal = str(oct(j))
        hexa = str(hex(j))
        binary = str(bin(j))
        o = ""
        h = ""
        b = ""

        for i in range(len(octal)):
            if i > 1:
                o = o + octal[i]

        for i in range(len(hexa)):
            if i > 1:
                h = h + hexa[i]

        for i in range(len(binary)):
            if i > 1:
                b = b + binary[i]

        print(str(j).rjust(a, " "), o.rjust(a, " "), h.upper().rjust(a, " "), b.rjust(a, " "))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
