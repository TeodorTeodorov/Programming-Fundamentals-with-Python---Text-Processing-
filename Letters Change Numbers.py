input = input().split()
num = ''
for string in input:
    for simbol in string:
        if simbol.isdigit():
            num += simbol
    for index in range(len(string)):
        if not string[index].isdigit():
            if string[index - 1].isupper():
                num = int(num) / ord(string[index - 1])
            else:
                num *= ord(string[index - 1])
            if string[index + 1].isupper():
                num = int(num) - ord(string[index + 1])
            else:
                num = int(num) + ord(string[index + 1])

print(num)
