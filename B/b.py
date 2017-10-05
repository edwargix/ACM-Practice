import math


chars = {
    "xxxxx"
    "x...x"
    "x...x"
    "x...x"
    "x...x"
    "x...x"
    "xxxxx":
    '0',

    "....x"
    "....x"
    "....x"
    "....x"
    "....x"
    "....x"
    "....x":
    '1',

    "xxxxx"
    "....x"
    "....x"
    "xxxxx"
    "x...."
    "x...."
    "xxxxx":
    '2',

    "xxxxx"
    "....x"
    "....x"
    "xxxxx"
    "....x"
    "....x"
    "xxxxx":
    '3',

    "x...x"
    "x...x"
    "x...x"
    "xxxxx"
    "....x"
    "....x"
    "....x":
    '4',

    "xxxxx"
    "x...."
    "x...."
    "xxxxx"
    "....x"
    "....x"
    "xxxxx":
    '5',

    "xxxxx"
    "x...."
    "x...."
    "xxxxx"
    "x...x"
    "x...x"
    "xxxxx":
    '6',

    "xxxxx"
    "....x"
    "....x"
    "....x"
    "....x"
    "....x"
    "....x":
    '7',

    "xxxxx"
    "x...x"
    "x...x"
    "xxxxx"
    "x...x"
    "x...x"
    "xxxxx":
    '8',

    "xxxxx"
    "x...x"
    "x...x"
    "xxxxx"
    "....x"
    "....x"
    "xxxxx":
    '9',

    "....."
    "..x.."
    "..x.."
    "xxxxx"
    "..x.."
    "..x.."
    ".....":
    '+'
}


def num_to_chars(numstr):
    if not numstr:
        return 0

    keys = []

    for digit in str(numstr):
        for key in chars.keys():
            if digit == chars[key]:
                keys.append(key)

    final = ''
    for l in range(7):
        pos = l * 5
        for key in keys:
            final += key[pos:pos+5] + '.'
        final = final[0:len(final) - 1]  # remove final period
        final += '\n'

    return final


def main():
    lines = []
    try:
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
    except EOFError:
        pass

    num_digits = math.ceil(len(lines[0]) / (5 + 1))
    buffers = [''] * num_digits

    for line in lines:
        i = 0
        while i < len(buffers):
            pos = i * (5 + 1)
            buffers[i] += line[pos:pos + 5]
            i += 1

    exp = ''
    for b in buffers:
        exp += chars[b]

    result = eval(exp)

    print(num_to_chars(result))  # super dangerous but meh


if __name__ == '__main__':
    main()
