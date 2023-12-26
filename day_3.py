
def read_file_into_matrix(file_path):

    matrix = []
    with open(file_path, 'r') as file:
        data = file.readlines()
        for line in data:
            matrix.append(list(line.strip()))

    return matrix


def main_part_one():
    matrix = read_file_into_matrix('files/day3.txt')
    symbol_map = {}

    tot_count = 0

    for r, row in enumerate(matrix):
        # print(row)
        nums, count = nums_in_row(matrix, r, symbol_map)
        tot_count += count

    print('Part 1', tot_count)
    return tot_count


def main_part_two():
    matrix = read_file_into_matrix('files/day3.txt')

    tot_count = 0

    symbol_map = {}

    for r, row in enumerate(matrix):
        _, _ = nums_in_row(matrix, r, symbol_map)

    for symbol in symbol_map:
        if symbol_map[symbol][0] == 2:
            ratio = symbol_map[symbol][1][0] * symbol_map[symbol][1][1]
            tot_count += ratio

    print('Part 2', tot_count)
    return tot_count


def nums_in_row(matrix, r, symbol_map):

    width = len(matrix[0])
    col = 0
    nums = []

    while col < width:
        if matrix[r][col].isdigit():
            num, end = finish_num(matrix, r, col)

            verified, symbols = verify_num(matrix, r, col, end)

            if verified:
                nums.append(num)

                for symbol in symbols:
                    if symbol not in symbol_map:
                        symbol_map[symbol] = [1, [num]]
                    else:
                        symbol_map[symbol][0] += 1
                        symbol_map[symbol][1].append(num)

            col = end + 1
        else:
            col += 1

    return nums, sum(nums)


def finish_num(matrix, r, c):

    init = c

    num_str = ''
    while c < len(matrix[0]) and matrix[r][c].isdigit():
        num_str += matrix[r][c]
        c += 1

    end_idx = init + len(num_str) - 1

    return int(num_str), end_idx


def verify_num(matrix, r, c1, c2):

    verified = False
    symbols = []

    for c in range(c1 - 1, c2 + 2):

        if 0 <= c < len(matrix[0]):
            # upper row
            if r + 1 < len(matrix) and matrix[r + 1][c] not in '.1234567890':
                symbols.append((r + 1, c))
                verified = True

            # lower row
            if r - 1 >= 0 and matrix[r - 1][c] not in '.1234567890':
                symbols.append((r - 1, c))
                verified = True

    # caps
    if c1 - 1 >= 0 and matrix[r][c1 - 1] not in '.1234567890':
        symbols.append((r, c1 - 1))
        verified = True

    if c2 + 1 < len(matrix[0]) and matrix[r][c2 + 1] not in '.1234567890':
        symbols.append((r, c2 + 1))
        verified = True

    return verified, symbols


if __name__ == '__main__':
    main_part_one()
    main_part_two()

# BAD STRATEGY

# def find_part_num(matrix, r, c):
#
#     nums = []
#
#     # left
#     try:
#         if matrix[r][c - 1].isdigit():
#             print('found num', matrix[r][c], 'at', r, c)
#             nums.append(get_full_num(matrix, r, c - 1))
#     except IndexError:
#         pass
#
#     # right
#     try:
#         if matrix[r][c + 1].isdigit():
#             print('found num', matrix[r][c], 'at', r, c)
#             nums.append(get_full_num(matrix, r, c + 1))
#     except IndexError:
#         pass
#
#     # top
#     try:
#         if matrix[r + 1][c].isdigit():
#             print('found num', matrix[r][c], 'at', r, c)
#             nums.append(get_full_num(matrix, r + 1, c))
#         else:
#             if matrix[r + 1][c + 1].isdigit():
#                 print('found num', matrix[r][c], 'at', r, c)
#                 nums.append(get_full_num(matrix, r + 1, c + 1))
#             if matrix[r + 1][c - 1].isdigit():
#                 print('found num', matrix[r][c], 'at', r, c)
#                 nums.append(get_full_num(matrix, r + 1, c - 1))
#     except IndexError:
#         pass
#
#     # bottom
#     try:
#         if matrix[r - 1][c].isdigit():
#             print('found num', matrix[r][c], 'at', r, c)
#             nums.append(get_full_num(matrix, r - 1, c))
#         else:
#             if matrix[r - 1][c + 1].isdigit():
#                 print('found num', matrix[r][c], 'at', r, c)
#                 nums.append(get_full_num(matrix, r - 1, c + 1))
#             if matrix[r - 1][c - 1].isdigit():
#                 print('found num', matrix[r][c], 'at', r, c)
#                 nums.append(get_full_num(matrix, r - 1, c - 1))
#     except IndexError:
#         pass
#
#     return sum(nums)
#
#
# def get_full_num(matrix, r, c):
#     row_len = len(matrix[0])
#     num_str = matrix[r][c]
#
#     steps = 1
#     while c - steps >= 0 and matrix[r][c - steps].isdigit():
#         num_str = matrix[r][c - steps] + num_str
#         steps += 1
#
#     steps = 1
#     while c + steps < row_len and matrix[r][c + steps].isdigit():
#         num_str = num_str + matrix[r][c + steps]
#         steps += 1
#
#     if steps > 1:
#         extension = True
#
#     print('complete num', num_str, 'at', r, c)
#
#     return int(num_str)
#
#
# def main():
#     matrix = read_file_into_matrix('files/day3.txt')
#
#     tot_count = 0
#
#     for r, row in enumerate(matrix):
#         for c, col in enumerate(row):
#             if matrix[r][c] not in '.1234567890':
#                 print('found symbol', matrix[r][c], 'at', r, c)
#                 tot_count += find_part_num(matrix, r, c)
#
#     print(tot_count)
#     return tot_count
#
#
