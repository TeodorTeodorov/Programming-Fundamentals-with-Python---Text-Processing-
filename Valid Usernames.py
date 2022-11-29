usernames = input().split(", ")

for name in usernames:
    is_valid = False
    if not ' ' in name:
        if 3 <= len(name) <= 16:
            for char in name:
                if char.isalnum() or char == '_' or char == '-':
                    is_valid = True
                break

    if is_valid:
        print(name)
