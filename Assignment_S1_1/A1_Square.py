
size = 6
for row in range(size):
    for col in range(size):
        if row == 0 or row == size - 1:
            print('*', row, end=' ')
        # if col == 0:
        #     print('*', end=' ')
    # if row > 0 or row < size - 1:
    #     print('*', row, end=' ')
    print()