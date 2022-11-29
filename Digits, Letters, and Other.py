
string = input()
digit = []
alfa = []
other = []

for ch in string:
    if ch.isdigit():
        digit.append(ch)

    elif ch.isalpha():
        alfa.append(ch)

    else:
        other.append(ch)

print(''.join(digit))
print(''.join(alfa))
print(''.join(other))