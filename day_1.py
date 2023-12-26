
def line_solver(input_string):
    char1 = None
    char2 = None
    first_index = -1

    for index, character in enumerate(input_string):
        if character.isdigit():
            char1 = character
            first_index = index
            break

    for index, character in enumerate(reversed(input_string)):
        if character.isdigit():
            char2 = character
            break
        if index >= len(input_string) - first_index - 1:
            break

    if char1 is None:
        return 0
    elif char2 is None:
        return int(char1) + 10*(int(char1))
    else:
        return 10 * (int(char1)) + int(char2)


def line_solver_two(input_string):

    char_to_num = {'one' : 1, 'two' : 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    char1 = None
    char2 = None
    first_index = -1
    second_index = -1

    for index, character in enumerate(input_string):
        if character.isdigit():
            char1 = character
            first_index = index
            break

    for index, character in enumerate(reversed(input_string)):
        if character.isdigit():
            char2 = character
            second_index = len(input_string) - index - 1
            break
        if index >= len(input_string) - first_index - 1:
            break

    for substring in char_to_num:
        position = input_string.find(substring)
        if position != -1 and (position < first_index or first_index == -1):
            char1 = substring
            first_index = position

        position = input_string.rfind(substring)
        if position != -1 and (position > second_index or second_index == -1):
            char2 = substring
            second_index = position

    if char1 is None:
        return 0
    elif char2 is None:
        if char1 in char_to_num:
            return char_to_num[char1] + 10*(char_to_num[char1])

        return int(char1) + 10 * (int(char1))
    else:
        if char1 in char_to_num:
            char1 = char_to_num[char1]
        else:
            char1 = int(char1)
        if char2 in char_to_num:
            char2 = char_to_num[char2]
        else:
            char2 = int(char2)

        return 10 * char1 + char2


def main():
    with open('files/day1.txt', 'r') as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        total += line_solver_two(line)

    print(total)


if __name__ == "__main__":
    main()

