## day 2 solution

def read_file_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    games = []

    for line in lines:
        draws = parse_line(line)
        games.append(draws)

    return games


def parse_line(line):

    stripped = line.split(':')
    draw_data = [draw.split(',') for draw in stripped[1].split(';')]

    draw_tuples = []
    for draw in draw_data:
        draw_tuple = [0, 0, 0]
        for pick in draw:
            pick_data = pick.strip().split(' ')
            count = pick_data[0]

            if pick_data[1] == 'red':
                draw_tuple[0] = int(count)
            if pick_data[1] == 'green':
                draw_tuple[1] = int(count)
            if pick_data[1] == 'blue':
                draw_tuple[2] = int(count)

        draw_tuples.append(draw_tuple)

    print(draw_tuples)
    return draw_tuples


def is_valid_game(draws, limits):

    for draw in draws:
        if draw[0] > limits[0] or draw[1] > limits[1] or draw[2] > limits[2]:
            return False

    return True


def main():
    games = read_file_data('files/day2.txt')

    counter = 0
    for i, g in enumerate(games):
        if is_valid_game(g, (12, 13, 14)):
            counter += i + 1
        else:
            print('invalid game', i + 1)

    print(counter)
    return counter


def power_of_game(draws):

    max_red = 0
    max_green = 0
    max_blue = 0

    for draw in draws:
        max_red = max(max_red, draw[0])
        max_green = max(max_green, draw[1])
        max_blue = max(max_blue, draw[2])

    return max_red * max_green * max_blue


def main2():
    games = read_file_data('files/day2.txt')

    counter = 0
    for i, g in enumerate(games):
        counter += power_of_game(g)

    print('Power sum:', counter)
    return counter


if __name__ == '__main__':
    main2()
