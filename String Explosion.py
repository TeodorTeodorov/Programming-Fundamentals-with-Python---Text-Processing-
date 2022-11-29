string = input()
explosion = 0
new_text = ''
for index in range(len(string)):
    if string[index] == '>':
        explosion += int(string[index +1])
        new_text += string[index]
    elif explosion > 0 and string[index] != '>':
        explosion -= 1

    else:
        new_text += string[index]
print(new_text)