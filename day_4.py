# day 4


def read_puzzle_input(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

    return lines


def get_line_data(line):
    line = line[line.find(":") + 1:]
    splitted = line.split("|")

    winning = splitted[0].strip().split(" ")
    elfs = splitted[1].strip().split(" ")

    winning = [int(x) for x in winning if x.isdigit()]
    elfs = [int(x) for x in elfs if x.isdigit()]

    return winning, elfs


def part_one():
    lines = read_puzzle_input('files/day4.txt')

    points = 0
    for line in lines:
        winning, elfs = get_line_data(line)

        card_points = 0
        for num in elfs:
            if num in winning:
                card_points += 1

        if card_points > 0:
            points += 2 ** (card_points - 1)

    print('Part 1', points)
    return points


def cards_won(winning, elfs):
    cards = 0

    for num in elfs:
        if num in winning:
            cards += 1

    return cards


def part_two():
    lines = read_puzzle_input('files/day4.txt')
    card_count = {}

    for card_no, line in enumerate(lines):
        winning, elfs = get_line_data(line)
        won = cards_won(winning, elfs)

        curr_card = card_no + 1
        additional = 1

        if curr_card in card_count:
            additional += card_count[curr_card]

        for i in range(curr_card + 1, curr_card + 1 + won):
            if i not in card_count:
                card_count[i] = additional
            else:
                card_count[i] += additional

        # print('Card:', curr_card, 'Won:', won)
        # print('Card count:', card_count)

    # print('Card count vals:', card_count.values())
    cards = sum(card_count.values())

    print('Part 2', cards + len(lines))
    return cards + len(lines)


if __name__  == '__main__':
    part_one()
    part_two()
