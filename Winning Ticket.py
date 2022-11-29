def len_valid_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_simbols = ['@', '#', '$', '^']
    left = ticket[:10]
    right = ticket[10:]
    # for simbols in winning_simbols:



def winning_ticket(ticket):
    count = 0
    if '@' or '#' or '$' or '^' in ticket:

        for simbol in ticket[:len(ticket) / 2]:
            if '@' in ticket:
                count += 1
                return count


current_ticket = input()


def main(current_ticket):
    result = winning_ticket(current_ticket)
    print(result)


current_ticket = [current_ticket.strip() for current_ticket in input().split(", ")]
for ticket in current_ticket:
    print(len_valid_ticket(ticket))
