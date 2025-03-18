def check_valid_number(count):
    while True:
        try:
            num = int(input(f'Enter input {count}: '))
            return num
        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue


def check_triangle():
    tri_sides =  [check_valid_number(count) for count in range(1, 4)]
    max_side = max(tri_sides)
    tri_sides.remove(max_side)
    sum_sides = sum(tri_sides)

    if sum_sides > max_side:
        return 'Yes, these three lengths can form a triangle.'
    else:
        return 'No, these three lengths cannot form a triangle.'

print(check_triangle())