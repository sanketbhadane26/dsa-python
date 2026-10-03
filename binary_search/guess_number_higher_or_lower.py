def guess(num, pick):

    if num == pick:
        return 0

    elif num > pick:
        return -1

    else:
        return 1


def guess_number(n, pick):

    left = 1
    right = n

    while left <= right:

        mid = (left + right) // 2

        result = guess(mid, pick)

        if result == 0:
            return mid

        elif result == -1:
            right = mid - 1

        else:
            left = mid + 1

    return -1


n = 10
pick = 6

result = guess_number(n, pick)

print(result)